import logging
from flask import Flask, json, request
import queryController

app = Flask(__name__)
app_path = '/api/'
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def hello_app():
    data = {'msg': 'Hello to Publication Graph RestApi'}
    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )


@app.route(app_path+'query1', methods=['GET'])
def query1():
    try:
        if not request.args.get('name'):
            raise Exception("missing {name} of author in query params")
        author_name = request.args['name']
        app.logger.info('Author name %s', author_name)
        return app.response_class(
            response=json.dumps(queryController.query1(author_name)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query2', methods=['GET'])
def query2():
    try:
        if not request.args.get('year') or not request.args.get('name'):
            raise Exception("missing {year} of publication or {name} of author in query params")
        year = request.args['year']
        name = request.args['name']
        app.logger.info('Particular year %s and name of author %s', year, name)
        return app.response_class(
            response=json.dumps(queryController.query2(name, year)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query3/conferences', methods=['GET'])
def query3_conferences():
    try:
        if not request.args.get('k'):
            raise Exception("missing {k} of top-K authors in query params")
        k = request.args['k']
        app.logger.info('Top-K %s', k)
        return app.response_class(
            response=json.dumps(queryController.query3_conferences(k)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query3/journals', methods=['GET'])
def query3_journals():
    try:
        if not request.args.get('k'):
            raise Exception("missing {k} of top-K authors in query params")
        k = request.args['k']
        app.logger.info('Top-K %s', k)
        return app.response_class(
            response=json.dumps(queryController.query3_journals(k)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query4', methods=['GET'])
def query4():
    try:
        if not request.args.get('k'):
            raise Exception("missing {k} of top-K authors in query params")
        k = request.args['k']
        app.logger.info('Top-K %s', k)
        return app.response_class(
            response=json.dumps(queryController.query4(k)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query5', methods=['GET'])
def query5():
    try:
        if not request.args.get('k') or not request.args.get('year'):
            raise Exception("missing {k} of top-K authors or particular {year} in query params")
        k = request.args['k']
        year = request.args['year']
        app.logger.info('Top-K %s and particular year %s', k, year)
        return app.response_class(
            response=json.dumps(queryController.query5(k, year)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query6', methods=['GET'])
def query6():
    try:
        if not request.args.get('k') :
            raise Exception("missing {k} of top-K authors in query params")
        k = request.args['k']
        app.logger.info('Top-K %s', k)
        return app.response_class(
            response=json.dumps(queryController.query6(k)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query7', methods=['GET'])
def query7():
    try:
        if not request.args.get('k') :
            raise Exception("missing {k} of top-K authors in query params")
        k = request.args['k']
        app.logger.info('Top-K %s', k)
        return app.response_class(
            response=json.dumps(queryController.query7(k)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query8', methods=['GET'])
def query8():
    try:
        if not request.args.get('k') :
            raise Exception("missing {k} of top-K authors in query params")
        k = request.args['k']
        app.logger.info('Top-K %s', k)
        return app.response_class(
            response=json.dumps(queryController.query8(k)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query9', methods=['GET'])
def query9():
    try:
        if not request.args.get('k') or not request.args.get('name'):
            raise Exception("missing {k} of top-K authors or particular {name} of author in query params")
        k = request.args['k']
        name = request.args['name']
        app.logger.info('Top-K %s and particular name %s', k, name)
        return app.response_class(
            response=json.dumps(queryController.query9(k, name)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query10', methods=['GET'])
def query10():
    try:
        if not request.args.get('year'):
            raise Exception("missing {year} of publication in query params")
        year = request.args['year']
        app.logger.info('Particular year %s', year)
        return app.response_class(
            response=json.dumps(queryController.query10(year)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query11', methods=['GET'])
def query11():
    try:
        if not request.args.get('year') or not request.args.get('name'):
            raise Exception("missing {year} of publication or {name} of author in query params")
        year = request.args['year']
        name = request.args['name']
        app.logger.info('Year %s and particular name %s', year, name)
        return app.response_class(
            response=json.dumps(queryController.query11(year, name)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query12/first', methods=['GET'])
def query12_first():
    try:
        if not request.args.get('year') or not request.args.get('journal'):
            raise Exception("missing {year} year or particular {journal} name in query params")
        year = request.args['year']
        journal = request.args['journal']
        app.logger.info('Year %s and particular journal name %s', year, journal)
        return app.response_class(
            response=json.dumps(queryController.query12_first(year, journal)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query12/last', methods=['GET'])
def query12_last():
    try:
        if not request.args.get('year') or not request.args.get('journal'):
            raise Exception("missing {year} year or particular {journal} name in query params")
        year = request.args['year']
        journal = request.args['journal']
        app.logger.info('Year %s and particular journal name %s', year, journal)
        return app.response_class(
            response=json.dumps(queryController.query12_last(year, journal)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query13', methods=['GET'])
def query13():
    try:
        if not request.args.get('journal'):
            raise Exception("missing particular {journal} name in query params")
        journal = request.args['journal']
        app.logger.info('Particular journal name %s', journal)
        return app.response_class(
            response=json.dumps(queryController.query13(journal)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query14', methods=['GET'])
def query14():
    try:
        return app.response_class(
            response=json.dumps(queryController.query14()),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query15', methods=['GET'])
def query15():
    try:
        if not request.args.get('k') :
            raise Exception("missing {k} of consecutive years in query params")
        k = request.args['k']
        app.logger.info('K consecutive years %s', k)
        return app.response_class(
            response=json.dumps(queryController.query15(k)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query16', methods=['GET'])
def query16():
    try:
        if not request.args.get('k') :
            raise Exception("missing {k} of top-K authors in query params")
        k = request.args['k']
        app.logger.info('Top-K %s', k)
        return app.response_class(
            response=json.dumps(queryController.query16(k)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query17', methods=['GET'])
def query17():
    try:
        if not request.args.get('years') :
            raise Exception("missing {years} in query params")
        years = request.args['years']
        app.logger.info('Amount of years %s', years)
        return app.response_class(
            response=json.dumps(queryController.query17(years)),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

@app.route(app_path+'query18', methods=['GET'])
def query18():
    try:
        return app.response_class(
            response=json.dumps(queryController.query18()),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return bad_request(str(e))

def bad_request(message):
    # app.logger.info(message)
    return json.dumps({'error':message}, default=str), 400, {'content-type':'application/json'}


if __name__ == '__main__':
    logging.info('Running on port %d, database is at %s', port, url)
    app.run(port=port)