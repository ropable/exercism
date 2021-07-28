#!/usr/bin/env bash

main () {
    # Set a default parameter value for the optional first input argument.
    # Ref: https://stackoverflow.com/questions/9332802/how-to-write-a-bash-script-that-takes-optional-input-arguments
    NAME=${1:-you}
    # Echo the message, substituting in the name parameter.
    echo "One for $NAME, one for me."
}

main "$@"
