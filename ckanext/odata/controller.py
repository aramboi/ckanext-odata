import ckan.plugins as p


class ODataController(p.toolkit.BaseController):

    def odata(self, uri):
        data_dict = {'uri': uri}
        action = p.toolkit.get_action('ckanext-odata_odata')
        result = action({}, data_dict)
        return result

    def odata_metadata(self):
        action = p.toolkit.get_action('ckanext-odata_metadata')
        result = action({},{})
        return result
