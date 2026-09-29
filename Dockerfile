FROM registry.access.redhat.com/ubi10/python-314-minimal:1790644478

RUN pip install --no-cache-dir flask

COPY --chown=1001:1001 app.py app.py

RUN echo "Information om företaget" > company.txt && \
    echo "Välkommen till webbservern" > welcome.txt && \
    echo "HR-uppgifter" > payroll.txt

CMD ["python", "app.py"]
