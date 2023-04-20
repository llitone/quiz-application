using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Tele2App.Model.QuizzisModels
{
    public class QuizAnswer
    {
        public QuizAnswer(Answer answer)
        {
            Id = answer.Id;
            QuestionId = answer.QuestionId;
            Text = answer.Text;
            IsCorrect = answer.IsCorrect;
            IsChecked = false;
        }
        public int Id { get; set; }
        public int QuestionId { get; set; }
        public string Text { get; set; }
        public bool IsCorrect { get; set; }
        public bool IsChecked { get; set; }
    }
}
