pipeline {
    agent any

    stages {
        stage('prepare_git') {
            steps {
                git branch: 'main', url: 'https://github.com/Electrotubbie/UrFU_MLOps_course'
            }
        }
        stage('prepare_venv') {
            steps {
                sh 'rm -R .venv/'
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('data_creation') {
            steps {
                sh 'python3 ./data_creation.py'
            }
        }
        stage('model_preprocessing') {
            steps {
                sh 'python3 ./model_preprocessing.py'
            }
        }
        stage('model_preparation') {
            steps {
                sh 'python3 ./model_preparation.py'
            }
        }
        stage('model_testing') {
            steps {
                sh 'python3 ./model_testing.py'
            }
        }
    }
}
