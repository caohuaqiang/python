if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5000,debug=True)
    # app.run()
    # app.run(debug=True)
    with open('chq.log', mode='a') as log:
        print(123, 'abc', file=log)
