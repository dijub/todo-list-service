from sqlalchemy import select
from sqlalchemy.orm import Session

from todo_list.models.user import User


def test_create_user(session: Session):
    new_user = User(
        username='diego', password='secret', email='diego@email.com'
    )
    session.add(new_user)
    session.commit()

    user: User | None = session.scalar(
        select(User).where(User.username == 'diego')
    )

    assert user is not None
    assert user.username == 'diego'
