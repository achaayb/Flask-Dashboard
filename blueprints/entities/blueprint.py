from flask import Blueprint, flash, redirect, render_template, request, url_for

from blueprints.entities.dao import entity_dao

blueprint = Blueprint("entities", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def entities():
    """
    Renders a list of entities and handles creation of new entities.
    """
    if request.method == "POST":
        name = request.form["name"]
        company = request.form["company"]
        city = request.form["city"]
        entity_dao.create_entity(name, company, city)
        flash("Created", "info")
        return redirect(url_for("entities.entities"))
    else:
        page_num = request.args.get('page', default=1, type=int)
        page = entity_dao.paginate(page=page_num)
        return render_template("entities/list_view.html", page=page)


@blueprint.route("/entities/create", methods=["GET"])
def create_entity():
    """
    Renders the form for creating a new entity.
    """
    return render_template("entities/create_view.html")


@blueprint.route("/entities/<string:id>", methods=["GET"])
def show_entity(id):
    """
    Renders the detail view for a specific entity.
    """
    entity = entity_dao.get_entity_by_id(id)
    if not entity:
        flash("Failed", "warning")
        return redirect(url_for("entities.entities"))

    return render_template("entities/detail_view.html", entity=entity)


@blueprint.route("/entities/<string:id>", methods=["GET", "POST"])
def edit_entity(id):
    """
    Renders the edit form for a specific entity and handles updating the entity.
    """
    entity = entity_dao.get_entity_by_id(id)
    if not entity:
        flash("Failed", "warning")
        return redirect(url_for("entities.entities"))

    if request.method == "POST":
        name = request.form["name"]
        company = request.form["company"]
        city = request.form["city"]
        entity_dao.update_entity(id, name, company, city)
        flash("Updated", "info")
        return redirect(url_for("entities.entities"))
    else:
        return render_template("entities/edit.html", entity=entity)


@blueprint.route("/entities/<string:id>/delete", methods=["POST"])
def delete_entity(id):
    """
    Deletes a specific entity.
    """
    success = entity_dao.delete_entity(id)
    if not success:
        flash("Failed", "warning")
        return redirect(url_for("entities.entities"))

    flash("Deleted", "info")
    return redirect(url_for("entities.entities"))
