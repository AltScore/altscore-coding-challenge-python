def process_batch_from_csv(csv_data, sources_config):
    """
    main function that takes the csv and returns the payload array.
    returns the payload array
    :return
    {
        "result": True|False (depending on if validation was successful)
        "payloads" List (the processed payloads)
    }
    """
    # validate if the columns in the csv comply with the required and atLeasOneRequired of each requested source
    # if validate == True
    #   compose the request body
    # else
    #   return false result and a None payload
    return {
        "result": True,
        "payload": [{}]
    }


def validate_inputs(field_list, sources_config):
    """
    validates that all required keys and all “at least one required” keys are present in the CSV for each
    of the sources listed in the sources_config.
    This return is recommended but not mandatory
    :return:
    {
     "result": True|False (depending on if validation was successful)
     "report": {
        "SOURCE-ID": {
            "required": True|False (depending on if all the required fields are in the field list),
            "at_leat_one_required": True|False (depending on if any of the atLeastOneRequired fields are in the field list)
        }
     }
    }
    """
    pass


def flatten_structure(input_keys_structure):
    """
    flatten the structure of the inputKeys
    it goes only one level deep (no source needs more than this)
    transforms {location: {lat: , lon: }} into [location.lat, location.lon]
    """
    pass


def compose_request_body(doc, sources_config):
    """
    this function composes the request body from the formatted JSON including just the sources that have all necessary
    data to run.
    """
    pass
