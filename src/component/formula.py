from data_model.table import T_Business_Formula

# class Indicator:
class Formula:
    @staticmethod
    def query(id):
        r = T_Business_Formula.query()
        return r

    @staticmethod
    def query_all():
        r = T_Business_Formula.query_all()
        return r
