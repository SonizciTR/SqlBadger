import os
from pyarrow import flight

class DremioService():
    def __init__(self) -> None:
        self.host = os.getenv("DREMIO_HOST")
        self.port = os.getenv("DREMIO_PORT")
        self.ldap_user = os.getenv("DREMIO_LDAP_USER")
        self.access_token = os.getenv("DREMIO_ACCESS_TOKEN")
        pass

    def run_query(self, query_sql : str) -> int:
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
        print(type(flight_table))
        df = flight_table.to_pandas()
        return len(df.index)