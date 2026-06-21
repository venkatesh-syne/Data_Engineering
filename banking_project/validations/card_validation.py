import apache_beam as beam


class ValidateCard(beam.DoFn):

    def process(self, record):

        try:

            if record["card_limit"] < 0:
                return

            yield record

        except Exception:
            pass