using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Tele2App.Model.QuizzisModels
{
    public class QuizQuestion
    {
        public QuizQuestion(Question question)
        {
            Id = question.Id;
            Age = question.Age;
            Text = question.Text;
            Difficulty = question.Difficulty;
            SubjectId = question.SubjectId;
            Explanation = question.Explanation;
            Points = question.Points;
            Answers = new();
            foreach(var answer in question.Answers)
            {
                Answers.Add(new QuizAnswer(answer));
            }
        }
        public int Id { get; set; }
        public int Age { get; set; }
        public string Text { get; set; }
        public int Difficulty { get; set; }
        public int Points { get; set; }
        public int SubjectId { get; set; }
        public string Explanation { get; set; }
        public List<QuizAnswer> Answers { get; set; }
    }
}
