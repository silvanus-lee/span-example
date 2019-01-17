train "pipeline_name_for_reference_within_span_config" {
    
    image = "python:3.7"
    install = ["pip install -r requirements.txt"]
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
