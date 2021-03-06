#! /bin/bash
# Parameter Handling for Script
helpFunction(){
    echo ""
    echo "Usage: $0 -p [path] -b [bucket-alias]"
    echo "Usage: $0 -p [path] -b [bucket-alias] [-c] [-f [*.pdf]]"
    echo -e "\t-p Specific path [required]"
    echo -e "\t-p Bucket alias [required]"
    echo -e "\t-f Filter file type [optional]"
    echo -e "\t-c Remove file after upload [optional]"
    echo ""
    exit 1 # Exit script after printing help
}
while getopts "p:b:f:c" opt
do
    case "$opt" in
        p ) readPath="$OPTARG" ;;
        b ) bucketAlias="$OPTARG" ;;
        f ) 
            if [[ ! -z "$OPTARG" ]]; then
                filterFile="$OPTARG"
            fi ;;
        c ) 
            if [[ ! -z "$OPTARG" ]]; then
                cleanUp=true
            else
                cleanUp=false
            fi ;;
        ? ) helpFunction ;;
    esac
done

Print helpFunction in case parameters are empty
if [ -z "$readPath" ] || [ -z "$bucketAlias" ]
then
    echo "Additional params required"
    helpFunction
fi

# Addtional Supporting Functions
remove_git(){
    cd ..
    echo "Removing: ./$path"
    rm -rf "./$path"
}
get_exe(){
    local file="$(basename $REPO)"
    local path="${file%%.*}"    
    rm -rf $path
    echo "Grabbing Repo: {$REPO}"
    git clone --quiet "$REPO"
    echo "Entering ./$path"
    cd "./$path"

}
clean_up(){
    local profile_name=""
}
file_upload(){
    echo "Writing to S3"

    if [ ! -z $filterFile ]
    then
        py UploadDirectory.py $readPath $bucketAlias $cleanUp $filterFile 
    else    
        py UploadDirectory.py $readPath $bucketAlias $cleanUp
    fi
}

cd "$readPath"
REPO="https://github.com/lovendatj/Notion-Integration.git"
echo $HOME
get_exe $REPO
file_upload
remove_git
