import torch
import torch.nn as nn
from torch_geometric.nn import GATConv


class Encoder(nn.Module):
    def __init__(self, input_channels=6, hidden_dim=64):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv1d(input_channels, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv1d(32, hidden_dim, kernel_size=3, padding=1),
            nn.AdaptiveAvgPool1d(1)
        )

    def forward(self, x):
        N, A, C, T = x.shape
        x = x.view(N * A, C, T)
        out = self.encoder(x).squeeze(-1)
        return out.view(N, A, -1)

class GATGraphLearner(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.gat = GATConv(input_dim, 1, add_self_loops=False, concat=False)

    def forward(self, x, adj_prior):
        N, A, D = x.shape
        pred_adj_list = []
        embeddings_list = []

        for i in range(N):
            xi = x[i]
            adj_i = adj_prior[i]
            edge_index = adj_i.nonzero(as_tuple=False).t()

            if edge_index.size(1) == 0:
                pred_adj_list.append(torch.zeros(A, A, device=x.device))
                embeddings_list.append(torch.zeros_like(xi))
                continue

            edge_weights = self.gat(xi, edge_index)
            edge_weights = torch.tanh(edge_weights)

            adj_out = torch.zeros(A, A, device=x.device)
            for idx, (src, dst) in enumerate(edge_index.t()):
                adj_out[src, dst] = edge_weights[idx]

            pred_adj_list.append(adj_out)
            embeddings_list.append(xi)

        return torch.stack(pred_adj_list), torch.stack(embeddings_list)

class SpeedPredictor(nn.Module):
    def __init__(self, input_dim, output_len=5):
        super().__init__()
        self.output_len = output_len
        self.predictor = nn.Sequential(
            nn.Linear(input_dim, input_dim),
            nn.ReLU(),
            nn.Linear(input_dim, 2 * output_len)
        )

    def forward(self, agent_embeddings):
        out = self.predictor(agent_embeddings)
        return out.view(out.shape[0], out.shape[1], 2, self.output_len)


class MotionGraphNet(nn.Module):
    def __init__(self, input_channels=6, T=20, hidden_dim=64):
        super().__init__()
        self.encoder = Encoder(input_channels, hidden_dim)
        self.graph_learner = GATGraphLearner(hidden_dim)
        self.speed_predictor = SpeedPredictor(hidden_dim, output_dim=2)

    def forward(self, agent_feats, adj_prior):
        encoded = self.encoder(agent_feats)
        pred_adj, embeddings = self.graph_learner(encoded, adj_prior)
        pred_speeds = self.speed_predictor(embeddings)
        return pred_adj, pred_speeds