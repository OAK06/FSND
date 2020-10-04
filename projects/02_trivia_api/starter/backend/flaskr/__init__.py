import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: -- DONE
  Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  ''' 
  CORS(app, resources={r"/api/*": {"origins": "*"}})
  
  ''' 
  Support Functions 
  '''
  def paginateResult(page, result):
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    formattedResult = [item.format() for item in result]
    return formattedResult[start:end]

  '''
  @TODO: -- DONE
  Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  '''
  @TODO: -- DONE
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories', methods=['GET', 'POST'])
  def getCategories():
    categories = Category.query.all()
    formattedCategories = {category.id: category.type for category in categories}
    return jsonify({
      'success': True,
      'categories': formattedCategories
    })

  '''
  @TODO: -- DONE
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions/<int:page>')
  def getQuestions(page):
    categories = Category.query.all()
    formattedCategories = {category.id: category.type for category in categories}
    questions = Question.query.all()
    formattedQuestions = paginateResult(page, questions)
    return jsonify({
      'success': True,
      'categories': formattedCategories,
      'questions': formattedQuestions,
      'total_questions': len(questions)
    })

  '''
  @TODO: -- DONE
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>/delete', methods=['DELETE'])
  def deleteQuestion(question_id):
    try:
      question = Question.query.get(question_id)
      question.delete()
      return jsonify({
          'success': True,
          'deleted': question_id
      })
    except:
      abort(422)

  '''
  @TODO: -- DONE
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def createQuestion():
    body = request.get_json()
    question = body.get('question')
    answer = body.get('answer')
    difficulty = body.get('difficulty')
    category = body.get('category')
    try:
      question = Question(question=question, answer=answer, difficulty=difficulty, category=category)
      question.insert()
      return jsonify({
          'success': True,
          'created': question.id,
      })
    except:
      abort(422)

  '''
  @TODO: -- DONE
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def searchQuestions():
    body = request.get_json()
    searchTerm = body.get('searchTerm', None)
    searchResults = Question.query.filter(Question.question.ilike(f'%{searchTerm}%')).all()
    return jsonify({
        'success': True,
        'questions': [question.format() for question in searchResults],
        'total_questions': len(searchResults),
        'current_category': None
    })

  '''
  @TODO: -- DONE
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def getCategoryQuestions(category_id):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    categories = Category.query.all()
    formattedCategories = {category.id: category.type for category in categories}
    questions = Question.query.filter(Question.category == category_id).all()
    formattedQuestions = paginateResult(page, questions)
    return jsonify({
      'success': True,
      'categories': formattedCategories,
      'current_category': category_id,
      'questions': formattedQuestions[start:end],
      'total_questions': len(questions)
    })

  '''
  @TODO: -- Done
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def playQuiz():
    try:
      body = request.get_json()
      category = body.get('quiz_category')
      previous_questions = body.get('previous_questions')
      if category['type'] == 'click':
        available_questions = Question.query.filter(Question.id.notin_((previous_questions))).all()
      else:
        available_questions = Question.query.filter_by(category=category['id']).filter(Question.id.notin_((previous_questions))).all()
      if len(available_questions) > 0:
        new_question = available_questions[random.randrange(0, len(available_questions))].format()  
      else:
        new_question = None

      return jsonify({
          'success': True,
          'question': new_question
      })
    except:
      abort(422)
  '''
  @TODO: -- Done
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(400)
  def badRequest(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "Bad Request"
    }), 400

  @app.errorhandler(404)
  def notFound(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "Resource not found"
    }), 404

  @app.errorhandler(422)
  def notProcessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "Not processable"
    }), 422

  @app.errorhandler(500)
  def badRequest(error):
    return jsonify({
      "success": False,
      "error": 500,
      "message": "Internal Server Error"
    }), 500

  return app

    