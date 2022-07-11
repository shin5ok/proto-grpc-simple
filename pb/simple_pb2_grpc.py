# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import simple_pb2 as simple__pb2


class SimpleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMessage = channel.unary_unary(
                '/simple.Simple/GetMessage',
                request_serializer=simple__pb2.Name.SerializeToString,
                response_deserializer=simple__pb2.Message.FromString,
                )
        self.PutMessage = channel.unary_unary(
                '/simple.Simple/PutMessage',
                request_serializer=simple__pb2.Message.SerializeToString,
                response_deserializer=simple__pb2.Name.FromString,
                )
        self.PingPong = channel.unary_unary(
                '/simple.Simple/PingPong',
                request_serializer=simple__pb2.Message.SerializeToString,
                response_deserializer=simple__pb2.Message.FromString,
                )
        self.ListMessage = channel.unary_stream(
                '/simple.Simple/ListMessage',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=simple__pb2.Message.FromString,
                )
        self.BulkPutMessage = channel.stream_unary(
                '/simple.Simple/BulkPutMessage',
                request_serializer=simple__pb2.Message.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class SimpleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PingPong(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BulkPutMessage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMessage,
                    request_deserializer=simple__pb2.Name.FromString,
                    response_serializer=simple__pb2.Message.SerializeToString,
            ),
            'PutMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.PutMessage,
                    request_deserializer=simple__pb2.Message.FromString,
                    response_serializer=simple__pb2.Name.SerializeToString,
            ),
            'PingPong': grpc.unary_unary_rpc_method_handler(
                    servicer.PingPong,
                    request_deserializer=simple__pb2.Message.FromString,
                    response_serializer=simple__pb2.Message.SerializeToString,
            ),
            'ListMessage': grpc.unary_stream_rpc_method_handler(
                    servicer.ListMessage,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=simple__pb2.Message.SerializeToString,
            ),
            'BulkPutMessage': grpc.stream_unary_rpc_method_handler(
                    servicer.BulkPutMessage,
                    request_deserializer=simple__pb2.Message.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'simple.Simple', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Simple(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simple.Simple/GetMessage',
            simple__pb2.Name.SerializeToString,
            simple__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simple.Simple/PutMessage',
            simple__pb2.Message.SerializeToString,
            simple__pb2.Name.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PingPong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/simple.Simple/PingPong',
            simple__pb2.Message.SerializeToString,
            simple__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/simple.Simple/ListMessage',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            simple__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BulkPutMessage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/simple.Simple/BulkPutMessage',
            simple__pb2.Message.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
