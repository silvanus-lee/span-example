version = "1.0"

train "wine_quality_trainer" {
    image = "python:3.7"
    install = ["pip install -r requirements-train.txt"]
    script = ["python3 train.py"]

    environment {
        ALPHA = 0.5
        L5_RATIO = 0.5
    }

    resources {
        cpu = 4
        memory = "8g"
    }

}

serve "wine_quality_server" {
    build {
        # see https://docs.docker.com/compose/compose-file/
        context = "."
        expose = [50051]
        # dockerfile = "Dockerfile-alternate"
    }

    resources {
        cpu = 2
        memory = "4g"
        replicas = 10
    }
}
