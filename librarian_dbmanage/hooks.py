from .dashboard_plugin import DBManageDashboardPlugin


def initialize(supervisor):
    supervisor.exts.dashboard.register(DBManageDashboardPlugin)
