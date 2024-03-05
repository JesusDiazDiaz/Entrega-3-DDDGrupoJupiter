from flask import Response

from src.properties.modules.listings.application.commands.recover_listings import RecoverListings
from src.properties.seedwork.presentation import api

from src.properties.seedwork.application.commands import execute_command

bp = api.crear_blueprint('properties', '/property')



@bp.route('/trigger', methods=('POST',))
def trigger():

    command = RecoverListings()

    execute_command(command)

    return Response('{}', status=202, mimetype='application/json')