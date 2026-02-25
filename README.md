# doc : comando : uv tool install --editable . hacer un cli comandos funcione 

- Agregar nueva migration
<p>alembic revision --autogenerate -m "add difference to user"</p> 

- Aplicar
<p>alembic upgrade head</p>

- Confirmar
<p>alembic current</p>