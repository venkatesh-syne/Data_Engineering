import apache_beam as beam


class ValidateAccount(beam.DoFn):

    def process(self, record):

        try:

            if record["balance"] < 0:
                return

            if record["status"] not in ["active", "inactive"]:
                return

            yield record

        except Exception:
            pass