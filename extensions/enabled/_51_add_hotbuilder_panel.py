# The name of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'hotbuilder'
# The name of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'project'
# The name of the panel group the PANEL is associated with.
PANEL_GROUP = 'orchestration'

ADD_INSTALLED_APPS = ['merlin', 'hotbuilder']

# Python panel class of the PANEL to be added.
ADD_PANEL = 'hotbuilder.panel.HotBuilderPanel'

ADD_ANGULAR_MODULES = ['merlin', 'hotbuilder']
ADD_JS_FILES = ['merlin/js/custom-libs/ui-bootstrap-tpls-0.12.1.js',
                'merlin/js/merlin.init.js',
                'merlin/js/merlin.templates.js',
                'hotbuilder/js/hotbuilder.init.js']
