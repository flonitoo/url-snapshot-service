pipeline {
  agent any

  environment {
    DOCKER_HUB_REPO      = "flonitoo/url-snapshot-service"
    DOCKERHUB_CREDENTIALS = 'dockerhub-creds'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          dockerImage = docker.build("${DOCKER_HUB_REPO}:${env.BUILD_NUMBER}")
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        script {
          docker.withRegistry('', DOCKERHUB_CREDENTIALS) {
            dockerImage.push("${env.BUILD_NUMBER}")
            dockerImage.push("latest")
          }
        }
      }
    }

    stage('Deploy (docker-compose)') {
      when {
        expression { return fileExists('docker-compose.yml') }
      }
      steps {
        sh 'docker-compose pull'
        sh 'docker-compose up -d --remove-orphans'
      }
    }
  }

  post {
    always {
      echo "Build finished: ${currentBuild.fullDisplayName}"
    }
  }
}
