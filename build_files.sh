# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

echo "Make migrations..."
python3.9 manage.py makemigrations
python3.9 manage.py migrate

echo "Collect static files..."
python3.9 manage.py collectstatic --noinput --clear
