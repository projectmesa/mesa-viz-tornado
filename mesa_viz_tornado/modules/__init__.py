"""
Container for all built-in visualization modules.
"""

from mesa_viz_tornado.modules.CanvasGridVisualization import CanvasGrid  # noqa
from mesa_viz_tornado.modules.ChartVisualization import ChartModule  # noqa
from mesa_viz_tornado.modules.PieChartVisualization import PieChartModule  # noqa
from mesa_viz_tornado.modules.BarChartVisualization import BarChartModule  # noqa
from mesa_viz_tornado.modules.HexGridVisualization import CanvasHexGrid  # noqa
from mesa_viz_tornado.modules.NetworkVisualization import NetworkModule  # noqa

# Delete this line in the next major release, once the simpler namespace has
# become widely adopted.
from mesa_viz_tornado.ModularVisualization import TextElement  # noqa
