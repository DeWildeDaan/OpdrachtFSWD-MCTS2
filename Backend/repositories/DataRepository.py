from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

# region ***  SQL STATEMENTS                        ***********

    # @staticmethod
    # def read_treinen():
    #     sql = "SELECT * FROM treinen"
    #     return Database.get_rows(sql)

    # @staticmethod
    # def read_trein(treinid):
    #     sql = "SELECT * FROM treinen WHERE idtrein = %s"
    #     params = [treinid]
    #     return Database.get_one_row(sql, params)

# endregion
