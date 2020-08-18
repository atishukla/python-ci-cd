#!groovy

node() {
	stage ('Checkout') {
	    checkout scm
	}


	stage ('Executing build') {
		docker.image('python:rc-slim').inside() {
		    sh 'python src/text-to-csv.py'
		}
	}

	stage ('Release') {
	    dir('resources') {
            archiveArtifacts artifacts: '**', fingerprint: true
        }
	    // echo "Current workspace is $WORKSPACE"
	}
}