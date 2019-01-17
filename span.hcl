train "pipeline_name_for_reference_within_span_config" {
    
    image = "python:3.7"
    install = ["pip install -r requirements.txt"]
    script = ["python3 train.py"]

    environment {
        DATABASE_URL = "mydb://user:pass@example.com/db"
        PARAM_1 = 10
        PARAM_2 = true
        PARAM_3 = "hello"
    }

    resources {
        cpu = 4
        memory = "8g"
    }
}
