# import packages
import numpy as np
import plotly.graph_objects as go
import scipy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D

from bezier import *


# sample bezier
mcp_num = 12
sample_control_points = np.random.uniform(-10, 10, size=(mcp_num, 2))
sample_bezier = bezier(control_points=sample_control_points)
sample_bezier_points = sample_bezier.get_points(num=100)

# init bezier control points - initial positions
cp_num = mcp_num * 2
sp_num = 1000
control_points = np.random.uniform(-10, 10, size=(cp_num, 2))
control_points[0] = sample_bezier_points[0]
control_points[-1] = sample_bezier_points[-1]
bezier_curve = bezier(control_points=control_points)
bezier_samples = bezier_curve.get_points(num=sp_num)

# # matplot setup
# colors = [[247/255, 66/255, 148/255], [86/255, 191/255, 117/255]]
# # print(colors)
# plt.figure(figsize=(8, 6), dpi=80)
# plt.ion()
# # optimization setup
# max_iteration = 10
# eps = 1
# offset_range = np.array([-5.0, 5.0])
# offset_range_decay = 0.999
# loss_recorder = []
# bezier_points_recorder = []
# total_loss = sys.float_info.max

# for i in range(max_iteration):
#     plt.cla()
#     plt.title("fitting curve")
#     plt.grid(True)
#     # test new  control points
#     select_id = np.random.randint(1, cp_num-1)
#     tmp_control_points = bezier_curve.get_control_points().copy()
#     tmp_control_points[select_id] += np.random.uniform(*offset_range, size=2)
#     tmp_curve = bezier(control_points=tmp_control_points)
#     tmp_loss = cal_loss(sample_points=sample_bezier_points,
#                         line_points=tmp_curve.get_points(num=sp_num))
#     # conclude discard or keep
#     if tmp_loss < total_loss:
#         # print(tmp_loss)
#         offset_range *= offset_range_decay
#         total_loss = tmp_loss
#         loss_recorder.append(total_loss)

#         # update fitting curve
#         bezier_curve.update_point(
#             id=select_id, value=tmp_control_points[select_id])
#         tmp_line_points = bezier_curve.get_points(num=sp_num)
#         bezier_points_recorder.append(tmp_line_points)
#         fitting_points_x = tmp_line_points[:, 0]
#         fitting_points_y = tmp_line_points[:, 1]
#         fitting_control_points_x = tmp_control_points[:, 0]
#         fitting_control_points_y = tmp_control_points[:, 1]
#         plt.scatter(sample_bezier_points[:, 0], sample_bezier_points[:, 1],
#                     c=[colors[0]], s=2.0, label="samples")
#         plt.scatter(sample_control_points[:, 0], sample_control_points[:, 1],
#                     c=[colors[0]], s=2.0, label="samples control points")
#         plt.plot(fitting_points_x, fitting_points_y,
#                  color=colors[1], linewidth=1.0, label="bezier curve")
#         plt.scatter(fitting_control_points_x, fitting_control_points_y,
#                     c=[colors[1]], s=4.0, label="control points")
#         plt.pause(0.001)
# plt.ioff()
# plt.show()


# print(np.array(bezier_points_recorder).shape)


# # Create figure
# fig = go.Figure(
#     data=[go.Scatter(x=control_points[:, 0], y=control_points[:, 1],
#                      marker=dict(color="red", size=10)),
#           go.Scatter(x=bezier_samples[:, 0], y=bezier_samples[:, 1],
#                      mode="lines",
#                      line=dict(width=2, color="green")),
#           go.Scatter(x=sample_control_points[:, 0],
#                      y=sample_control_points[:, 1],
#                      marker=dict(color="red", size=10)),
#           go.Scatter(x=sample_bezier_points[:, 0], y=sample_bezier_points[:, 1],
#                      marker=dict(color="red", size=10))],
#     layout=go.Layout(
#         title_text="Fitting Curve", hovermode="closest",
#         updatemenus=[dict(type="buttons",
#                           buttons=[dict(label="Play",
#                                         method="animate",
#                                         args=[None])])]),
#     frames=[go.Frame(
#         data=[go.Scatter(
#             x=[xx[k]],
#             y=[yy[k]],
#             mode="markers",
#             marker=dict(color="red", size=10)),
#             go.Scatter(
#             x=[xx[k]],
#             y=[yy[k]+1],
#             mode="markers",
#             marker=dict(color="green", size=10))])

#             for point in bezier_points_recorder]
# )

# fig.show()
