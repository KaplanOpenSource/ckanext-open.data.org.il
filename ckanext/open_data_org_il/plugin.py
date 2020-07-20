import ckan.plugins as plugins
from ckan.plugins.toolkit import add_template_directory, add_public_directory, add_resource, get_action


PLUGIN_CACHE = {}


class OpenDataOrgIlPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        add_template_directory(config, 'templates')
        add_public_directory(config, 'public')
        add_resource('fanstatic', 'open_data_org_il')

    def get_settings_group(self, *args, **kwargs):
        if "settings_group" not in PLUGIN_CACHE:
            PLUGIN_CACHE["settings_group"] = get_action("group_show")(data_dict={
                "id": "settings",
                "include_extras": True,
                "include_dataset_count": False, "include_users": False, "include_groups": False, "include_tags": False,
                "include_followers": False
            })
        return PLUGIN_CACHE["settings_group"]

    def get_helpers(self):
        return {'settings': self.get_settings_group}
