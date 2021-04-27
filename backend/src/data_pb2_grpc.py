# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_pb2 as data__pb2


class IRStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/ir.search.IR/CreateUser',
                request_serializer=data__pb2.User.SerializeToString,
                response_deserializer=data__pb2.User.FromString,
                )
        self.AutoCreateUser = channel.unary_stream(
                '/ir.search.IR/AutoCreateUser',
                request_serializer=data__pb2.Empty.SerializeToString,
                response_deserializer=data__pb2.User.FromString,
                )
        self.QueryES = channel.unary_stream(
                '/ir.search.IR/QueryES',
                request_serializer=data__pb2.QueryRequest.SerializeToString,
                response_deserializer=data__pb2.ResultEntry.FromString,
                )
        self.QueryCustom = channel.unary_stream(
                '/ir.search.IR/QueryCustom',
                request_serializer=data__pb2.QueryRequest.SerializeToString,
                response_deserializer=data__pb2.ResultEntry.FromString,
                )
        self.ReadBook = channel.unary_unary(
                '/ir.search.IR/ReadBook',
                request_serializer=data__pb2.UsageData.SerializeToString,
                response_deserializer=data__pb2.User.FromString,
                )
        self.RateBook = channel.unary_unary(
                '/ir.search.IR/RateBook',
                request_serializer=data__pb2.UsageData.SerializeToString,
                response_deserializer=data__pb2.User.FromString,
                )


class IRServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AutoCreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryES(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryCustom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RateBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IRServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=data__pb2.User.FromString,
                    response_serializer=data__pb2.User.SerializeToString,
            ),
            'AutoCreateUser': grpc.unary_stream_rpc_method_handler(
                    servicer.AutoCreateUser,
                    request_deserializer=data__pb2.Empty.FromString,
                    response_serializer=data__pb2.User.SerializeToString,
            ),
            'QueryES': grpc.unary_stream_rpc_method_handler(
                    servicer.QueryES,
                    request_deserializer=data__pb2.QueryRequest.FromString,
                    response_serializer=data__pb2.ResultEntry.SerializeToString,
            ),
            'QueryCustom': grpc.unary_stream_rpc_method_handler(
                    servicer.QueryCustom,
                    request_deserializer=data__pb2.QueryRequest.FromString,
                    response_serializer=data__pb2.ResultEntry.SerializeToString,
            ),
            'ReadBook': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadBook,
                    request_deserializer=data__pb2.UsageData.FromString,
                    response_serializer=data__pb2.User.SerializeToString,
            ),
            'RateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.RateBook,
                    request_deserializer=data__pb2.UsageData.FromString,
                    response_serializer=data__pb2.User.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ir.search.IR', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IR(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ir.search.IR/CreateUser',
            data__pb2.User.SerializeToString,
            data__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AutoCreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ir.search.IR/AutoCreateUser',
            data__pb2.Empty.SerializeToString,
            data__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryES(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ir.search.IR/QueryES',
            data__pb2.QueryRequest.SerializeToString,
            data__pb2.ResultEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryCustom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ir.search.IR/QueryCustom',
            data__pb2.QueryRequest.SerializeToString,
            data__pb2.ResultEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ir.search.IR/ReadBook',
            data__pb2.UsageData.SerializeToString,
            data__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ir.search.IR/RateBook',
            data__pb2.UsageData.SerializeToString,
            data__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
