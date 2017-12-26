const express = require('express');
const router = express.Router();

//let Poll = require('../models/polls');

// Add question home Route
router.post('/', function (req, res) {

    const id = req.body.id;
    const answer = req.body.answer;
    req.checkBody('id', 'pollquestion is required').notEmpty();
    req.checkBody('answer', 'pollcategory is required').notEmpty();

     //description
     let anyErrors = req.validationErrors();
         if (anyErrors) {
           // does nothing
             return ;
         }
         else {
            Poll
            .findById(id, function (err, pollToChange) {
                if (err) return handleError(err);
                pollToChange.answers.push({ answer: answer, stats: { users: [], votes: 0 } })
    
                pollToChange.save(function (err, updatedPollToChange) {
                    if (err) return handleError(err);
                    res.send(updatedPollToChange);
                });
            });
        }
});

module.exports = router;