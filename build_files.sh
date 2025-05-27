echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Making migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Build completed."
