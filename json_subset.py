import copy

class Validate():

    ANY = '_any'

    def __init__(self):

        pass

    def is_subset(self, subset, superset):

        subset = copy.deepcopy(subset)
        superset = copy.deepcopy(superset)
        
        if isinstance(subset, dict) and isinstance(superset, dict):
            for subset_key in subset:
                if subset_key not in superset:
                    return False

                superset_val = superset[subset_key]
                subset_val = subset[subset_key]

                if not self.is_subset(subset_val, superset_val):
                    return False

            return True

        elif isinstance(subset, list):

            if subset and subset[0] == self.ANY:
                for subset_val in subset[1:]:
                    if self.is_subset(subset_val, superset):
                        return True

            elif isinstance(superset, list):
                for subset_val in subset:
                    list_found = False 
                    for superset_val in superset:
                        if self.is_subset(subset_val, superset_val):
                            list_found = True
                            break

                    if not list_found:
                        return False

                return True

        elif isinstance(subset, (str, unicode)) and isinstance(superset, (str, unicode)):
            return subset == superset

        elif type(subset) == type(superset) and isinstance(superset, (int, float)):
            return subset == superset

        elif superset == None and subset == None:
            return True

        return False
