"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
brand_8 = Brand.query.get(8);

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corv_chev = db.session.query(Model).filter(Model.name == "Corvette",
                                           Model.brand_name == "Chevrolet").all()

# Get all models that are older than 1960.
old_models = db.session.query(Model).filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
old_brands = db.session.query(Brand).filter(Brand.founded < 1920).all()

# Get all models with names that begin with "Cor".
cor_models = db.session.query(Model).filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
brands_1903 = db.session.query(Brand).filter(Brand.founded == 1903,
                                             Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
brands_old_or_discontinued = db.session.query(Brand).filter(db.or_(Brand.founded < 1950,
                                                                   Brand.discontinued.isnot(None))).all()
# Get any model whose brand_name is not Chevrolet.
models_no_chev = db.session.query(Model).filter(Model.brand_name != "Chevrolet").all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    model_info = db.session.query(Model.name,
                                  Model.brand_name,
                                  Brand.headquarters).join(Brand).filter(Model.year == year).all()

    # Check to make sure that the query populated the list,
    # else print "No results."
    if model_info:
        # For each tuple item in the list created by .all(), print the info
        for info in model_info:
            print ("Model: {}\tBrand: {}\tHQ: {}").format(info[0], info[1], info[2])
    else:
        print ("No results.")
    pass


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
    using only ONE database query.'''
    brands_summary = db.session.query(Brand.name,
                                      Model.name).join(Model).group_by(Model.name, Brand.name).order_by(Brand.name).all()

    if brands_summary:
        for item in brands_summary:
            print ("{}: {}".format(item[0], item[1]))
    else:
        print ("No results.")

    pass

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# The statement above returns a Query object, which is part of the SQLAlchemy
# library. A Query is an iterable object. Because this particular the query
# is being executed on the Brand as a whole (instead of a single field of Brand
# being indicated), the Brand objects are returned.

# No SQL is issued when the statement above is executed. If you want the SQL to
# immediately execute and to return the result of the Query, another method should
# be chained onto that statement (typically all(), first(), or one()).

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An associateion table sits between two other tables and is created for the
# sole purpose of indicating the relationships between those two other tables.
# It typically might contain only its own primary key field and two foreign
# keys tied to the other tables. It is managing a many-to-many relationship
# between the two other tables, which means that it itself has a many-to-one
# relationship with each table.



# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """Returns list of Brand objects which have names containing the input."""
    return db.session.query(Brand).filter(Brand.name.like('%'+mystr+'%')).all()


def get_models_between(start_year, end_year):
    """Returns list of Models between years indicated (including start_year,
        excluding end_year)"""
    return db.session.query(Model).filter(Model.year >= start_year,
                                          Model.year < end_year).all()
