import json

from flask import redirect, render_template, request, session, url_for
from flask import Response

from src.auditoria.seedwork.presentation import api
from src.auditoria.seedwork.domain.exceptions import DomainException

from src.auditoria.modules.enrequicimiento.application.mapper import PropertyDTOJson
from src.auditoria.modules.enrequicimiento.application.services import PropertyService

from src.auditoria.modules.enrequicimiento.application.commands.update_information import UpdateInformation
from src.auditoria.seedwork.application.commands import execute_command

bp = api.crear_blueprint('audit', '/audit')


@bp.route('/', methods=('PUT',))
def information():
    try:
        property_dict = request.json

        map_property = PropertyDTOJson()
        property_dto = map_property.externo_a_dto(property_dict)

        command = UpdateInformation(
            property_dto.size_sqft,
            property_dto.construction_type,
            property_dto.floors
        )

        execute_command(command)

        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
