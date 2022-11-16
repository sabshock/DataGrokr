pipeline{
    agent{
        label  "agent_lin"}
    stages {
        stage ('git-checkout'){
            steps{
                sh 'echo Checking out git Repo'
                git branch: 'python', url: 'https://github.com/sabshock/DataGrokr.git'
            }

        }

        stage ('Test') {
            
            steps{
                sh'echo "Runing Unit test"'    
                sh 'python3 start.py'
            }

        }
    }
}
