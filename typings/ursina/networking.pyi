"""
This type stub file was generated by pyright.
"""

from enum import Enum

"""
This type stub file was generated by pyright.
"""
class Connection:
    def __init__(self, peer, socket, address, connection_timeout) -> None:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def send(self, data):
        ...
    
    def disconnect(self):
        ...
    
    def is_timed_out(self):
        ...
    
    def is_connected(self):
        ...
    


class PeerEvent(Enum):
    ERROR = ...
    CONNECT = ...
    DISCONNECT = ...
    DATA = ...


class PeerInput(Enum):
    ERROR = ...
    SEND = ...
    DISCONNECT = ...
    DISCONNECT_ALL = ...


class Peer:
    def __init__(self, on_connect=..., on_disconnect=..., on_data=..., on_raw_data=..., connection_timeout=..., use_tls=..., path_to_certchain=..., path_to_private_key=..., path_to_cabundle=..., socket_address_family=...) -> None:
        ...
    
    def is_using_tls(self):
        ...
    
    def start(self, host_name, port, is_host=..., backlog=..., tls_host_name=..., socket_address_family=...):
        ...
    
    def stop(self):
        ...
    
    def update(self, max_events=...):
        ...
    
    def send(self, connection, data):
        ...
    
    def disconnect(self, connection):
        ...
    
    def disconnect_all(self):
        ...
    
    def is_running(self):
        ...
    
    def is_hosting(self):
        ...
    
    def connection_count(self):
        ...
    
    def get_connections(self):
        ...
    


class DatagramWriter:
    def __init__(self) -> None:
        ...
    
    def register_type(self, the_type, write_func):
        ...
    
    def clear(self):
        ...
    
    def get_datagram(self):
        ...
    
    def write(self, value):
        ...
    
    def write_string(self, value):
        ...
    
    def write_string32(self, value):
        ...
    
    def write_bool(self, value):
        ...
    
    def write_int8(self, value):
        ...
    
    def write_int16(self, value):
        ...
    
    def write_int32(self, value):
        ...
    
    def write_int64(self, value):
        ...
    
    def write_float32(self, value):
        ...
    
    def write_float64(self, value):
        ...
    
    def write_blob(self, value):
        ...
    
    def write_blob32(self, value):
        ...
    


class ExceedsListLimitException(Exception):
    ...


class DatagramReader:
    def __init__(self) -> None:
        ...
    
    def register_type(self, the_type, read_func):
        ...
    
    def set_datagram(self, datagram):
        ...
    
    def get_datagram(self):
        ...
    
    def set_datagram_from_blob(self, blob):
        ...
    
    def read(self, value_type, max_list_length=...):
        ...
    
    def read_string(self):
        ...
    
    def read_string32(self):
        ...
    
    def read_bool(self):
        ...
    
    def read_int8(self):
        ...
    
    def read_int16(self):
        ...
    
    def read_int32(self):
        ...
    
    def read_int64(self):
        ...
    
    def read_float32(self):
        ...
    
    def read_float64(self):
        ...
    
    def read_blob(self):
        ...
    
    def read_blob32(self):
        ...
    


def procedure_hash(name):
    ...

class RPCPeer:
    def __init__(self, max_list_length=..., **kwargs) -> None:
        ...
    
    def is_using_tls(self):
        ...
    
    def start(self, host_name, port, is_host=..., backlog=..., tls_host_name=..., socket_address_family=...):
        ...
    
    def stop(self):
        ...
    
    def update(self, max_events=...):
        ...
    
    def is_running(self):
        ...
    
    def is_hosting(self):
        ...
    
    def disconnect_all(self):
        ...
    
    def connection_count(self):
        ...
    
    def get_connections(self):
        ...
    
    def register_type(self, the_type, write_func, read_func):
        ...
    
    def register_procedure(self, proc, host_only=..., client_only=..., prefix=...):
        ...
    
    def __getattr__(self, name):
        ...
    
    def rpc_on_data(self, connection, data, time_received):
        ...
    


def rpc(peer, host_only=..., client_only=...):
    ...

