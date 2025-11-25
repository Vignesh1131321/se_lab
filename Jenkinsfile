pipeline {
    agent any

    environment {
        IMAGE = "vignesh1131321/imt2023003:jenkins"
        VENV = ".venv"
        // Ensure Python 3.13 installation path is available to the pipeline
        PATH = "${env.PATH};C:\\Program Files\\Python313"
        // Define the Python path once here
        PYTHON = "C:\\Program Files\\Python313\\python.exe"
        // Make sure this ID matches what is in your Jenkins Credentials
        DOCKER_CRED  = 'docker-jenkins' 
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[
                    url: 'https://github.com/Vignesh1131321/se_lab.git',
                    // Ensure this ID exists in Jenkins credentials
                    credentialsId: 'github-creds'
                  ]]
                ])
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '''
                    REM Use the variable defined at the top, quoted for safety
                    "%PYTHON%" -m venv .venv
                    call %VENV%\\Scripts\\activate
                    python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    call %VENV%\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call %VENV%\\Scripts\\activate
                    REM ensure pytest is installed if not in requirements.txt
                    pip install pytest 
                    pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE% ."
            }
        }

        stage('Push Docker Image') {
            steps {
                // Now using the env.DOCKER_CRED variable defined at the top
                withCredentials([usernamePassword(credentialsId: env.DOCKER_CRED,
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    bat '''
                        echo %PASS% | docker login -u %USER% --password-stdin
                        docker push %IMAGE%
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                    docker pull %IMAGE%
                    docker stop ci-cd-demo || true
                    docker rm ci-cd-demo || true
                    docker run -d -p 5000:5000 --name ci-cd-demo %IMAGE%
                '''
            }
        }
    }
}