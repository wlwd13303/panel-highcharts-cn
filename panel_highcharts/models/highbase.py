"""Contains the Bokeh Model for the HighBase pane"""
from collections import OrderedDict

from bokeh.core.properties import Any, Dict, Nullable, String
from bokeh.models import LayoutDOM
from panel.util import classproperty

PATH_HIGH_CHARTS = "https://code.highcharts.com.cn/highcharts.js"
PATH_REQUIRE_HIGH_CHARTS = "https://code.highcharts.com.cn"

PATHS = OrderedDict(
    [
        ("highcharts-3d", "https://code.highcharts.com.cn/highcharts/highcharts-3d.js"),
        ("highcharts-more", "https://code.highcharts.com.cn/highcharts/highcharts-more.js"),
        ("highcharts/modules/stock", "https://code.highcharts.com.cn/modules/stock.js"),
        ("highcharts/modules/map", "https://code.highcharts.com.cn/maps/modules/map.js"),
        ("highcharts/modules/coloraxis", "https://code.highcharts.com.cn/maps/modules/coloraxis.js"),
        (
            "highcharts/modules/marker-clusters",
            "https://code.highcharts.com.cn/maps/modules/marker-clusters.js",
        ),
        ("highcharts/modules/gantt", "https://code.highcharts.com.cn/modules/gantt.js"),
        ("highcharts/modules/exporting", "https://code.highcharts.com.cn/modules/exporting.js"),
        ("highcharts/modules/export-data", "https://code.highcharts.com.cn/modules/export-data.js"),
        ("highcharts/modules/networkgraph", "https://code.highcharts.com.cn/modules/networkgraph.js"),
        ("highcharts/modules/annotations", "https://code.highcharts.com.cn/modules/annotations.js"),
        ("highcharts/modules/boost", "https://code.highcharts.com.cn/modules/boost.js"),
        ("highcharts/modules/broken-axis", "https://code.highcharts.com.cn/modules/broken-axis.js"),
        ("highcharts/modules/canvas-tools", "https://code.highcharts.com.cn/modules/canvas-tools.js"),
        ("highcharts/modules/data", "https://code.highcharts.com.cn/modules/data.js"),
        ("highcharts/modules/drilldown", "https://code.highcharts.com.cn/modules/drilldown.js"),
        ("highcharts/modules/funnel", "https://code.highcharts.com.cn/modules/funnel.js"),
        ("highcharts/modules/heatmap", "https://code.highcharts.com.cn/modules/heatmap.js"),
        (
            "highcharts/modules/no-data",
            "https://code.highcharts.com.cn/modules/no-data-to-display.js",
        ),
        (
            "highcharts/modules/offline-exporting",
            "https://code.highcharts.com.cn/modules/offline-exporting.js",
        ),
        ("highcharts/modules/solid-gauge", "https://code.highcharts.com.cn/modules/solid-gauge.js"),
        ("highcharts/modules/treemap", "https://code.highcharts.com.cn/modules/treemap.js"),
        ("highcharts/modules/variwide", "https://code.highcharts.com.cn/modules/variwide.js"),
    ]
)


class HighBase(LayoutDOM):
    """The Bokeh Model for the HighBase pane"""

    config = Nullable(Dict(String, Any))
    config_update = Nullable(Dict(String, Any))
    _add_series = Nullable(Dict(String, Any))

    # Events
    event = Nullable(Dict(String, Any))

    __javascript__ = [
        "https://code.highcharts.com.cn/highcharts.js",
        "https://code.highcharts.com.cn/modules/export-data.js",
        "https://code.highcharts.com.cn/modules/exporting.js",
        "https://code.highcharts.com.cn/highcharts-plugins/highcharts-zh_CN.js",
    ]

    @classproperty
    def __js_skip__(cls) -> Dict:  # pylint: disable=no-self-argument
        return {
            "highcharts": cls.__javascript__,
        }

    # https://api.highcharts.com/class-reference/#toc5
    __js_require__ = {
        "packages": [
            {
                "name": "highcharts",
                "main": "highcharts",
            },
        ],
        "paths": {
            "highcharts": "https://code.highcharts.com",
            "highcharts/modules/exporting": "https://code.highcharts.com.cn/modules/exporting",
            "highcharts/modules/export-data": "https://code.highcharts.com.cn/modules/export-data",
        },
        "exports": {
            "highcharts": "Highcharts",
            "highcharts/modules/exporting": "highchartsmodulesexporting",
            "highcharts/modules/export-data": "highchartsmodulesexportdata",
        },
    }
