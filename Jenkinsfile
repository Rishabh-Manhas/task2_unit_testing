pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Rishabh-Manhas/task2_unit_testing.git']])
            }
        }
        stage('Build step') {
            steps {
                
                sh 'python test_case.py'
            }
        }
        
    }
}
