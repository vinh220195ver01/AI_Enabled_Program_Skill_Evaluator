(function () {
  'use strict';

  var MAX_REVIEW_LENGTH = 500;
  var STORAGE_KEY = 'myshop.commenter';
  var EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Reviews for this product. Status is "pending" until a moderator approves it.
  var reviews = [
    {
      id: 1,
      author: 'Anna K.',
      rating: 5,
      comment: 'Great fit and the fabric feels really soft. Washed it several times and it still looks new.',
      date: 'September 14, 2026',
      status: 'approved'
    },
    {
      id: 2,
      author: 'David L.',
      rating: 4,
      comment: 'Good quality for the price. The colour is slightly lighter than in the photo.',
      date: 'September 29, 2026',
      status: 'approved'
    },
    {
      id: 3,
      author: 'Mai T.',
      rating: 3,
      comment: 'Comfortable, but it runs a little small. I would order one size up next time.',
      date: 'October 8, 2026',
      status: 'approved'
    }
  ];
  var nextId = 4;

  var selectedStar = null; // index of the selected star button (0-4)

  var el = {
    form: document.getElementById('review-form'),
    stars: Array.prototype.slice.call(document.querySelectorAll('#star-input .star')),
    ratingValue: document.getElementById('rating-value'),
    comment: document.getElementById('comment'),
    charCount: document.getElementById('char-count'),
    name: document.getElementById('name'),
    email: document.getElementById('email'),
    saveInfo: document.getElementById('save-info'),
    errors: document.getElementById('form-errors'),
    success: document.getElementById('form-success'),
    list: document.getElementById('review-list'),
    noReviews: document.getElementById('no-reviews'),
    heading: document.getElementById('reviews-heading'),
    summaryStars: document.getElementById('summary-stars'),
    summaryText: document.getElementById('summary-text'),
    pendingCount: document.getElementById('pending-count'),
    approveBtn: document.getElementById('approve-btn'),
    moderatorMsg: document.getElementById('moderator-msg')
  };

  // ---------- helpers ----------

  function starsMarkup(container, value) {
    container.textContent = '';
    for (var i = 1; i <= 5; i++) {
      var s = document.createElement('span');
      s.textContent = '★';
      if (i > value) {
        s.className = 'off';
      }
      container.appendChild(s);
    }
  }

  function formatDate(d) {
    return d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
  }

  function approvedReviews() {
    return reviews.filter(function (r) { return r.status === 'approved'; });
  }

  function pendingReviews() {
    return reviews.filter(function (r) { return r.status === 'pending'; });
  }

  // ---------- rendering ----------

  function renderSummary() {
    var approved = approvedReviews();
    var total = approved.reduce(function (sum, r) { return sum + r.rating; }, 0);
    var count = reviews.length;
    var average = count ? total / count : 0;

    starsMarkup(el.summaryStars, Math.round(average));
    if (count === 0) {
      el.summaryText.textContent = 'No ratings yet';
    } else {
      el.summaryText.textContent = average.toFixed(1) + ' out of 5 – based on ' +
        count + (count === 1 ? ' review' : ' reviews');
    }
  }

  function renderReviews() {
    var approved = approvedReviews().slice().sort(function (a, b) { return b.id - a.id; });

    el.heading.textContent = 'Reviews (' + approved.length + ')';
    el.list.textContent = '';
    el.noReviews.hidden = approved.length > 0;

    approved.forEach(function (r) {
      var li = document.createElement('li');
      li.className = 'review-item';

      var meta = document.createElement('div');
      meta.className = 'review-meta';

      var stars = document.createElement('span');
      stars.className = 'stars-static';
      stars.setAttribute('aria-label', r.rating + ' out of 5 stars');
      starsMarkup(stars, r.rating);

      var author = document.createElement('span');
      author.className = 'review-author';
      author.textContent = r.author;

      var date = document.createElement('span');
      date.className = 'review-date';
      date.textContent = r.date;

      meta.appendChild(stars);
      meta.appendChild(author);
      meta.appendChild(date);

      var text = document.createElement('p');
      text.className = 'review-text';
      text.textContent = r.comment;

      li.appendChild(meta);
      li.appendChild(text);
      el.list.appendChild(li);
    });
  }

  function renderModerator() {
    var pending = pendingReviews().length;
    el.pendingCount.textContent = String(pending);
    el.approveBtn.disabled = pending === 0;
  }

  function renderAll() {
    renderSummary();
    renderReviews();
    renderModerator();
  }

  // ---------- star rating input ----------

  function paintStars(upTo, cls) {
    el.stars.forEach(function (btn, i) {
      btn.classList.toggle(cls, upTo !== null && i <= upTo);
    });
  }

  function setRating(index) {
    selectedStar = index;
    paintStars(selectedStar, 'selected');
    el.stars.forEach(function (btn, i) {
      btn.setAttribute('aria-checked', String(i === index));
    });
    if (index === null) {
      el.ratingValue.textContent = '';
    } else {
      var n = index + 1;
      el.ratingValue.textContent = n + (n === 1 ? ' star' : ' stars');
    }
  }

  el.stars.forEach(function (btn) {
    var index = Number(btn.getAttribute('data-index'));
    btn.addEventListener('click', function () { setRating(index); });
    btn.addEventListener('mouseenter', function () { paintStars(index, 'hover'); });
    btn.addEventListener('mouseleave', function () { paintStars(null, 'hover'); });
  });

  // ---------- form ----------

  function updateCharCount() {
    el.charCount.textContent = String(el.comment.value.length);
  }

  el.comment.addEventListener('input', updateCharCount);

  function showErrors(messages) {
    el.success.hidden = true;
    el.errors.textContent = '';
    var ul = document.createElement('ul');
    messages.forEach(function (m) {
      var li = document.createElement('li');
      li.textContent = m;
      ul.appendChild(li);
    });
    el.errors.appendChild(ul);
    el.errors.hidden = false;
  }

  function showSuccess(message) {
    el.errors.hidden = true;
    el.errors.textContent = '';
    el.success.textContent = message;
    el.success.hidden = false;
  }

  function readForm() {
    return {
      comment: el.comment.value.trim(),
      name: el.name.value.trim(),
      email: el.email.value.trim()
    };
  }

  function validate(data) {
    var errors = [];
    if (!selectedStar) {
      errors.push('Please select a rating.');
    }
    if (data.comment.length === 0) {
      errors.push('Please write your review.');
    } else if (data.comment.length >= MAX_REVIEW_LENGTH) {
      errors.push('Your review must be ' + MAX_REVIEW_LENGTH + ' characters or fewer.');
    }
    if (data.name.length === 0) {
      errors.push('Please enter your name.');
    }
    if (data.email.length === 0) {
      errors.push('Please enter your email address.');
    } else if (!EMAIL_PATTERN.test(data.email)) {
      errors.push('Please enter a valid email address.');
    }
    return errors;
  }

  function createReview(data) {
    return {
      id: nextId++,
      author: data.email,
      name: data.name,
      rating: selectedStar + 1,
      comment: data.comment,
      date: formatDate(new Date()),
      status: 'pending'
    };
  }

  function rememberCommenter(data) {
    try {
      if (el.saveInfo.checked) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify({ name: data.name, email: data.email }));
      } else {
        localStorage.removeItem(STORAGE_KEY);
      }
    } catch (e) {
      // storage not available; nothing to remember
    }
  }

  function restoreCommenter() {
    try {
      var saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
      if (saved) {
        el.name.value = saved.name || '';
        el.email.value = saved.email || '';
        el.saveInfo.checked = true;
      }
    } catch (e) {
      // ignore unreadable storage
    }
  }

  el.form.addEventListener('submit', function (event) {
    event.preventDefault();
    var data = readForm();
    var errors = validate(data);
    if (errors.length) {
      showErrors(errors);
      return;
    }

    reviews.push(createReview(data));
    rememberCommenter(data);

    el.comment.value = '';
    updateCharCount();
    setRating(null);
    if (!el.saveInfo.checked) {
      el.name.value = '';
      el.email.value = '';
    }

    showSuccess('Thank you! Your review has been submited and is awaiting approval.');
    el.moderatorMsg.textContent = '';
    renderAll();
  });

  // ---------- moderator ----------

  el.approveBtn.addEventListener('click', function () {
    var pending = pendingReviews();
    pending.forEach(function (r) { r.status = 'approved'; });
    el.moderatorMsg.textContent = pending.length + (pending.length === 1 ? ' review' : ' reviews') + ' approved.';
    renderAll();
  });

  // ---------- init ----------

  restoreCommenter();
  updateCharCount();
  renderAll();
})();
