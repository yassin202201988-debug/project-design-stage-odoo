FROM odoo:17.0

USER root

COPY ./project_design_stage /mnt/extra-addons/project_design_stage
COPY ./project_design_stage_demo /mnt/extra-addons/project_design_stage_demo

USER odoo