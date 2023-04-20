using Tele2App.Model;
using Tele2App.Model.QuizzisModels;
using Tele2App.View;

namespace Tele2App.ViewModel
{
    public class QuestionViewModel : BaseViewModel
    {
        public event Action StopTimer;
        public Question Question { get; set; }
        public QuizQuestion QuizQuestion { get; set; }

        public QuestionViewModel(Question question)
        {
            Question = question;
            QuizQuestion = new QuizQuestion(question);
        }

        public ButtonCommand Answer
        {
            get
            {
                return new ButtonCommand(async () =>
                {
                    StopTimer?.Invoke();
                    bool isCorrect = Check(QuizQuestion);
                    if (isCorrect)
                        Current.CurrentUser.GetUser().Points += QuizQuestion.Points;
                    await Shell.Current.GoToAsync(nameof(MainPage));
                });
            }
        }

        private bool Check(QuizQuestion question)
        {
            foreach(var answer in question.Answers)
            {
                if (answer.IsChecked != answer.IsCorrect)
                    return false;
            }
            return true;
        }
    }
}
