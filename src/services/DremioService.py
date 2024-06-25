import os
from pyarrow import flight, Table

from models.QueryResult import QueryResult

class DremioService():
    def __init__(self) -> None:
        self.host = os.getenv("DREMIO_HOST")
        self.port = os.getenv("DREMIO_PORT")
        self.ldap_user = os.getenv("DREMIO_LDAP_USER")
        self.access_token = os.getenv("DREMIO_ACCESS_TOKEN")
        pass

    def run_query(self, query_sql : str) -> QueryResult:
        raw_succ =  False
        count_affected = 0 
        msg = ""

        try:
            # Construct the Flight Client
            client = flight.FlightClient('grpc://' + self.host + ':' + self.port, disable_server_verification=True)

            # Authenticate
            bearer_token = client.authenticate_basic_token(self.ldap_user, self.access_token)
            options = flight.FlightCallOptions(headers=[bearer_token])

            # Query
            info = client.get_flight_info(flight.FlightDescriptor.for_command(query_sql),
                                        options)
            reader = client.do_get(info.endpoints[0].ticket, options)

            # Get the Query Output and write to pandas df
            flight_table = reader.read_all()
            
            count_affected = flight_table.num_rows
            raw_succ = self.safe_get_pyarrowtable(flight_table, 'ok', 'False')
            msg = self.safe_get_pyarrowtable(flight_table, 'summary', '[No Message]')
        except Exception as e:
            raw_succ = False
            msg = str(e)

        return QueryResult(bool(raw_succ), msg, count_affected)
    
    def safe_get_pyarrowtable(self, table_data : Table, clm_name : str, default_value : any = None) -> str:
        if(clm_name not in table_data.column_names): return default_value

        if(table_data.num_rows < 1): return default_value


        return table_data.column(clm_name)[0].as_py()