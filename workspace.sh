cd $1
mkdir -p $2
cd $2

if [ -z "$4" ] && [ -z "$5" ]
then
    touch $3
else
    touch $3 && touch $4 && touch $5
fi

echo "Workspace created sucessfuly!"
echo ""