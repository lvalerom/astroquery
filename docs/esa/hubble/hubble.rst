.. doctest-skip-all

.. _astroquery.esa.hubble:

*****************************************
ESA HST Archive (`astroquery.esa.hubble`)
*****************************************

The Hubble Space Telescope (HST) is a joint ESA/NASA orbiting astronomical
observatory operating from the near-infrared into the ultraviolet.  Launched
in 1990 and scheduled to operate at least through 2020, HST carries and has
carried a wide variety of instruments producing imaging, spectrographic,
astrometric, and photometric data through both pointed and parallel
observing programs. During its lifetime HST has become one of the most
important science projects ever, with over 500 000 observations of more than
30000 targets available for retrieval from the Archive.

This package allows the access to the `European Space Agency Hubble Archive
<http://archives.esac.esa.int/ehst/>`__. All the HST observations available
in the EHST are synchronised with the MAST services for HST reprocessed
public data and corresponding metadata.  Therefore, excluding proprietary
data, all HST data in the EHST are identical to those in MAST.

========
Examples
========

--------------------------
1. Getting Hubble products
--------------------------

This function allows the user to download products based on their observation ID (mandatory) and
a required calibration_level (RAW, CALIBRATED, PRODUCT or AUXILIARY) and/or product type (PRODUCT,
SCIENCE_PRODUCT or POSTCARD).

This will download all files for the raw calibration level of the observation 'J6FL25S4Q' and it will store them in a tar called
'raw_data_for_J6FL25S4Q.tar'.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> esahubble.download_product(observation_id="J6FL25S4Q", calibration_level="RAW", filename="raw_data_for_J6FL25S4Q.tar")

This will download the science files associated to the observation 'J6FL25S4Q' and it will store them in a file called
'science_data_for_J6FL25S4Q.tar.fits.gz', modifying the filename provided to ensure that the extension of the file is correct.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> esahubble.download_product(observation_id="J6FL25S4Q", filename="science_data_for_J6FL25S4Q.tar", product_type="SCIENCE_PRODUCT")

This third case will download the science files associated to the observation 'J6FL25S4Q' in raw calibration level and it will store them in a file called
'science_raw_data_for_J6FL25S4Q.fits.gz', modifying the filename provided to ensure that the extension of the file is correct.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> esahubble.download_product(observation_id="J6FL25S4Q", calibration_level="RAW", filename="science_raw_data_for_J6FL25S4Q", product_type="SCIENCE_PRODUCT")

---------------------------
2. Getting Hubble postcards
---------------------------

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> esahubble.get_postcard("J6FL25S4Q", "RAW", 256, "raw_postcard_for_J6FL25S4Q.jpg")

This will download the postcard for the observation 'J8VP03010' with low
resolution (256) and it will stored in a jpg called
'raw_postcard_for_J6FL25S4Q.jpg'. Resolution of 1024 is also available.

Calibration levels can be RAW, CALIBRATED, PRODUCT or AUXILIARY.

---------------------------
3. Getting Hubble artifacts
---------------------------

Note: Artifact is a single Hubble product file.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> esahubble.get_artifact("w0ji0v01t_c2f.fits.gz")

This will download the compressed artifact
'w0ji0v01t_c2f.fits.gz'. 'w0ji0v01t_c2f.fits' is the name of the Hubble
artifact to be download.

----------------------------------------------
4. Querying target names in the Hubble archive
----------------------------------------------

The query_target function queries the name of the target as given by the proposer of the observations.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> table = esahubble.query_target("m31", "m31_query.xml")
  >>> str(table)

This will retrieve a table with the output of the query.
It will also download a file storing all metadata for all observations
associated with target name 'm31'. The result of the query will be stored in
file 'm31_query.xml'.

-----------------------------------------------------------------
5. Querying observations by search criteria in the Hubble archive
-----------------------------------------------------------------

The query_criteria function uses a set of established parameters to create
and execute an ADQL query, accessing the HST archive database usgin the Table
Access Protocol (TAP). 

- **calibration_level** (*str or int, optional*): The identifier of the data reduction/processing applied to the data.

 + RAW (1)
 + CALIBRATED (2)
 + PRODUCT (3)
 + AUXILIARY (0)

- **data_product_type** (*str, optional*): High level description of the product.

 + image
 + spectrum 
 + timeseries

- **intent** (*str, optional*): The intent of the original obsever in acquiring this observation.

 + SCIENCE 
 + CALIBRATION

- **collection** (*list of strings, optional*): List of collections that are available in eHST catalogue.

 + HLA
 + HST
 
 Do not forget that this is a list of elements, so it must be defined as ['HST'], ['HST', 'HLA']...
 
- **instrument_name** (*list of strings, optional*): Name(s) of the instrument(s) used to generate the dataset. This is also a list of elements.
- **filters** (*list of strings, optional*): Name(s) of the filter(s) used to generate the dataset. This is also a list of elements.
- **async_job** (*bool, optional, default 'True'*): executes the query (job) in asynchronous/synchronous mode (default synchronous)
- **output_file** (*str, optional, default None*) file name where the results are saved if dumpToFile is True. If this parameter is not provided, the jobid is used instead
- **output_format** (*str, optional, default 'votable'*) results format
- **verbose** (*bool, optional, default 'False'*): flag to display information about the process
- **get_query** (*bool, optional, default 'False'*): flag to return the query associated to the criteria as the result of this function.

This is an example of a query with all the parameters and the verbose flag activated, so the query is shown as a log message.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> result = esahubble.query_criteria(calibration_level = 3,
                                        data_product_type = 'image',
                                        intent='SCIENCE',
                                        obs_collection=['HLA'],
                                        instrument_name = ['WFC3'],
                                        filters = ['F555W', 'F606W'],
                                        async_job = False,
                                        output_file = 'output1.vot.gz',
                                        output_format="votable",
                                        verbose = True,
                                        get_query = False)
  INFO: select o.*, p.calibration_level, p.data_product_type from ehst.observation 
  AS o LEFT JOIN ehst.plane as p on o.observation_uuid=p.observation_uuid
  where(p.calibration_level LIKE '%PRODUCT%' AND p.data_product_type LIKE '%image%'
  AND o.intent LIKE '%SCIENCE%' AND (o.collection LIKE '%HLA%') AND (o.instrument_name
  LIKE '%WFC3%') AND (o.instrument_configuration LIKE '%F555W%' OR
  o.instrument_configuration LIKE '%F606W%')) [astroquery.esa.hubble.core]
  >>> str(result)
  Table length=2000 ...
  
This will make a synchronous search, limited to 2000 results to find the observations that match these specific
requirements. It will also download a votable file called **output.vot.gz** containing the result of the
query.

The following example uses the string definition of the calibration level ('PRODUCT') and executes an asynchronous job to get all the results that match the criteria.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> result = esahubble.query_criteria(calibration_level = 'PRODUCT', 
                                        data_product_type = 'image', 
                                        intent='SCIENCE', 
                                        obs_collection=['HLA'], 
                                        instrument_name = ['WFC3'], 
                                        filters = ['F555W', 'F606W'], 
                                        async_job = True, 
                                        output_file = 'output2.vot.gz', 
                                        output_format="votable", 
                                        verbose = True, 
                                        get_query = False)
  >>> str(result)
  Table length=12965 ...
  
As has been mentioned, these parameters are optional and it is not necessary to define all of them to execute this function, as the search will be adapted to the ones that are available.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> result1 = esahubble.query_criteria(calibration_level = 'PRODUCT', 
                                         async_job = False, 
                                         output_file = 'output3.vot.gz')
  >>> result2 = esahubble.query_criteria(data_product_type = 'image', 
                                         intent='SCIENCE', 
                                         async_job = False, 
                                         output_file = 'output4.vot.gz')
  >>> result3 = esahubble.query_criteria(data_product_type = 'timeseries',
                                         async_job = False, 
                                         output_file = 'output5.vot.gz')
 
If no criteria are specified to limit the selection, this function will retrieve all the observations.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> result = esahubble.query_criteria(async_job = False, 
                                        verbose = True)
  INFO: select o.*, p.calibration_level, p.data_product_type from ehst.observation
  AS o LEFT JOIN ehst.plane as p on o.observation_uuid=p.observation_uuid
  [astroquery.esa.hubble.core]

 This last example will provide the ADQL query based on the criteria defined by the user.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> result = esahubble.query_criteria(calibration_level = 'PRODUCT',
                                        data_product_type = 'image',
                                        intent='SCIENCE',
                                        obs_collection=['HLA'],
                                        instrument_name = ['WFC3'],
                                        filters = ['F555W', 'F606W'],
                                        get_query = True)
  >>> str(result)

--------------------------------------
6. Cone searches in the Hubble archive
--------------------------------------

.. code-block:: python

  >>> from astropy import coordinates
  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> c = coordinates.SkyCoord("00h42m44.51s +41d16m08.45s", frame='icrs')
  >>> table = esahubble.cone_search(c, 7, "cone_search_m31_5.vot")
  >>> str(table)

This will perform a cone search with radius 7 arcmins. The result of the
query will be returned and stored in the votable file
'cone_search_m31_5.vot'. If no filename is defined and the "save" tag is True,
the module will provide a default name. It is also possible to store only the results
in memory, without defining neither a filename nor the "save" tag.

----------------------------------------------------
7. Cone searches with criteria in the Hubble archive
----------------------------------------------------

It is also possible to perform a cone search defined by a target name or coordinates, a radius
and a set of criteria to filter the results.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> result = esahubble.cone_search_criteria(target= 'm31',radius=7,
                                              obs_collection=['HST'],
                                              data_product_type = 'image',
                                              instrument_name = ['ACS/WFC'],
                                              filters = ['F435W'],
                                              async_job = True,
                                              filename = 'output1.vot.gz',
                                              output_format="votable")
  >>> result

    <Table length=302>
    algorithm_name collection         end_time           end_time_mjd   exposure_duration ... target_name calibration_level data_product_type         ra                dec
        object       object            object              float64           float64      ...    object         object            object           float64            float64
    -------------- ---------- ----------------------- ----------------- ----------------- ... ----------- ----------------- ----------------- ------------------ -----------------
           drizzle        HST 2002-06-29 14:15:20.787 52454.51065725694            1600.0 ...      M31-T3        CALIBRATED             image 10.791884595154517 41.28819762447081
               ...        ...                     ...               ...               ... ...         ...               ...               ...                ...               ...
          exposure        HST   2014-06-26 03:40:17.0 56834.06964120371            1246.0 ...   M-31-CORE        CALIBRATED             image 10.531742116262286 41.25273489574185
          exposure        HST   2014-06-26 03:40:17.0 56834.06964120371            1246.0 ...   M-31-CORE               RAW             image 10.531742116262286 41.25273489574185


.. code-block:: python

  >>> from astropy import coordinates
  >>> from astropy import units as u
  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> c = coordinates.SkyCoord("00h42m44.51s +41d16m08.45s", frame='icrs')
  >>> result = esahubble.cone_search_criteria(coordinates=c,radius=7*u.arcmin,
                                              obs_collection=['HST'],
                                              instrument_name = ['WFPC2'],
                                              filters = ['F606W'],
                                              async_job = True,
                                              filename = 'output1.vot.gz',
                                              output_format="votable",
                                              verbose=True)
  >>> str(table)

This will perform a cone search with radius 7 arcmins around the target (defined by
its coordinates or its name) using the filters defined when executing the function.

This function allows the same parameters than the search criteria (see Section 5).


-------------------------------
8. Getting access to catalogues
-------------------------------

This function provides access to the HST archive database using the Table
Access Protocol (TAP) and via the Astronomical Data Query Language (ADQL).

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> result = esahubble.query_hst_tap("select top 10 * from hsc_v2.hubble_sc2", "test.vot.gz")
  >>> print(result)

This will execute an ADQL query to download the first 10 sources in the
Hubble Source Catalog (HSC) version 2.1 (format default: compressed
votable). The result of the query will be stored in the file
'test.vot.gz'. The result of this query can be viewed by doing
result.get_results() or printing it by doing print(result).


------------------------------------------------------
9. Getting related members of HAP and HST observations
------------------------------------------------------

This function takes in an observation id of a Composite or Simple observation.
If the observation is Simple the method returns the Composite observation that
is built on this simple observation. If the observation is Composite then the
method returns the simple observations that make it up.

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> result = esahubble.get_member_observations("jdrz0c010")
  >>> print(result)


--------------------------------------------------------
10. Getting link between Simple HAP and HST observations
--------------------------------------------------------

This function takes in an observation id of a Simple HAP or HST observation and
returns the corresponding HAP or HST observation

.. code-block:: python

  >>> from astroquery.esa.hubble import ESAHubble
  >>> esahubble = ESAHubble()
  >>> result = esahubble.get_hap_hst_link("hst_16316_71_acs_sbc_f150lp_jec071i9")
  >>> print(result)



Reference/API
=============

.. automodapi:: astroquery.esa.hubble
    :no-inheritance-diagram:
