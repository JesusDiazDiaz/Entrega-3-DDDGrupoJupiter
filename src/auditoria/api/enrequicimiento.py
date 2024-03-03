import json

from flask import redirect, render_template, request, session, url_for
from flask import Response

from src.auditoria.modules.enrequicimiento.application.queries.get_low_reliability_information import \
    GetLowReliabilityInformation
from src.auditoria.seedwork.presentation import api
from src.auditoria.seedwork.domain.exceptions import DomainException

from src.auditoria.modules.enrequicimiento.application.mapper import PropertyDTOJson

from src.auditoria.modules.enrequicimiento.application.commands.update_information import UpdateInformation
from src.auditoria.seedwork.application.commands import execute_command
from src.auditoria.seedwork.application.queries import execute_query

bp = api.crear_blueprint('audit', '/audit')


@bp.route('/low', methods=('GET',))
def low():
    query_result = execute_query(GetLowReliabilityInformation())

    map_property = PropertyDTOJson()
    result = [map_property.dto_to_external(info) for info in query_result.result]

    return result

@bp.route('/', methods=('PUT',))
def information():
    try:
        property_dict = request.json

        map_property = PropertyDTOJson()
        property_dto = map_property.external_to_dto(property_dict)

        command = UpdateInformation(
            property_dto.id,
            property_dto.size_sqft,
            property_dto.construction_type,
            property_dto.floors
        )

        execute_command(command)

        return Response('{}', status=202, mimetype='application/json')
    except DomainException as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
