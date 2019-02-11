import logging

import grpc

import serve_pb2
import serve_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        client = serve_pb2_grpc.WineQualityPredictorStub(channel)

        response = client.PredictQuality(
            serve_pb2.PredictRequest(
                fixed_acidity=9,
                volatile_acidity=0.19,
                citric_acid=0.3,
                residual_sugar=2,
                chlorides=0.053,
                free_sulfur_dioxide=48,
                total_sulfur_dioxide=140,
                density=0.994,
                ph=3.180,
                sulphates=0.490,
                alcohol=9.6,
            )
        )

    print("Wine quality client received: " + str(response.quality))


if __name__ == "__main__":
    logging.basicConfig()
    run()
