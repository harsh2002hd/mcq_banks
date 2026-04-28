import React, { useState, useMemo, useEffect } from 'react';
import { BookOpen, ChevronLeft, ChevronRight, Shuffle, Home, Hash, CheckCircle, XCircle, AlertCircle, Settings, Save, Loader2 } from 'lucide-react';
import data from './data/questions.json';
import './index.css';

const OPTION_LABELS = ['A', 'B', 'C', 'D'];

function App() {
  const [selectedSubject, setSelectedSubject] = useState(null);
  const [currentIndex, setCurrentIndex]       = useState(0);
  const [jumpTo, setJumpTo]                   = useState('');
  const [isShuffled, setIsShuffled]           = useState(false);
  const [selectedOption, setSelectedOption]   = useState(null);
  const [answered, setAnswered]               = useState(false);
  const [score, setScore]                     = useState({ correct: 0, total: 0 });
  const [editMode, setEditMode]               = useState(false);
  const [saving, setSaving]                   = useState(false);
  const [saveMessage, setSaveMessage]         = useState({ text: '', type: '' });

  // Reset when subject changes
  useEffect(() => {
    setCurrentIndex(0);
    setJumpTo('');
    setIsShuffled(false);
    setSelectedOption(null);
    setAnswered(false);
    setScore({ correct: 0, total: 0 });
  }, [selectedSubject]);

  // Reset answer state when changing question
  useEffect(() => {
    setSelectedOption(null);
    setAnswered(false);
  }, [currentIndex]);

  const questions = useMemo(() => {
    if (!selectedSubject) return [];
    let qs = [...selectedSubject.questions];
    if (isShuffled) {
      for (let i = qs.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [qs[i], qs[j]] = [qs[j], qs[i]];
      }
    }
    return qs;
  }, [selectedSubject, isShuffled]);

  const currentQuestion = questions[currentIndex];

  const handleSubjectSelect = (subjectId) => {
    setSelectedSubject(data.subjects.find(s => s.id === subjectId));
  };

  const handleNext = () => {
    if (currentIndex < questions.length - 1) setCurrentIndex(p => p + 1);
  };
  const handlePrev = () => {
    if (currentIndex > 0) setCurrentIndex(p => p - 1);
  };

  const handleOptionClick = (index) => {
    if (answered) return;
    setSelectedOption(index);
    setAnswered(true);
    setScore(prev => ({
      correct: prev.correct + (index === currentQuestion.correctAnswerIndex ? 1 : 0),
      total:   prev.total + 1,
    }));
  };

  const handleJump = (e) => {
    e.preventDefault();
    const idx = parseInt(jumpTo) - 1;
    if (!isNaN(idx) && idx >= 0 && idx < questions.length) {
      setCurrentIndex(idx);
      setJumpTo('');
    }
  };

  const toggleShuffle = () => {
    setIsShuffled(s => !s);
    setCurrentIndex(0);
  };

  const handleSaveCorrection = async (newIdx) => {
    setSaving(true);
    setSaveMessage({ text: '', type: '' });
    try {
      const response = await fetch('/api/save-answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          subjectId: selectedSubject.id,
          questionId: currentQuestion.id,
          correctAnswerIndex: newIdx
        })
      });
      const result = await response.json();
      if (result.success) {
        // Update local data so it reflects immediately
        currentQuestion.correctAnswerIndex = newIdx;
        currentQuestion.hasDetectedAnswer = true;
        setSaveMessage({ text: 'Saved successfully!', type: 'success' });
        setTimeout(() => setSaveMessage({ text: '', type: '' }), 3000);
      } else {
        setSaveMessage({ text: 'Error: ' + result.error, type: 'error' });
      }
    } catch (err) {
      setSaveMessage({ text: 'Failed to save to disk.', type: 'error' });
    } finally {
      setSaving(false);
    }
  };

  const getOptionClass = (idx) => {
    if (editMode) {
      return idx === currentQuestion.correctAnswerIndex ? 'correct' : '';
    }
    if (!answered) return '';
    if (idx === currentQuestion.correctAnswerIndex) return 'correct';
    if (idx === selectedOption) return 'incorrect';
    return 'disabled';
  };

  return (
    <div className="app-container">
      <header className="header">
        <div>
          <h1 className="text-gradient" style={{ fontSize: '2.2rem', display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <BookOpen size={38} /> Aviation MCQ Pro
          </h1>
          <p style={{ color: 'var(--text-secondary)', marginTop: '0.25rem' }}>Master your aviation knowledge</p>
        </div>
        {selectedSubject && (
          <button className="btn btn-icon" onClick={() => setSelectedSubject(null)} title="Back to Home">
            <Home size={24} />
          </button>
        )}
      </header>

      {!selectedSubject ? (
        /* ── HOME: subject grid ── */
        <div className="glass-panel">
          <h2 style={{ marginBottom: '1.5rem', fontSize: '1.5rem' }}>Select a Subject</h2>
          <div className="subjects-grid">
            {data.subjects.map(subject => (
              <div
                key={subject.id}
                className="glass-panel subject-card"
                onClick={() => handleSubjectSelect(subject.id)}
              >
                <div style={{ fontSize: '2.5rem', marginBottom: '0.5rem' }}>{subject.icon || '📚'}</div>
                <h3 className="subject-title">{subject.name}</h3>
                <p className="subject-desc">{subject.description}</p>
                <div style={{ marginTop: '1rem', color: 'var(--primary-color)', fontSize: '0.85rem', fontWeight: '600' }}>
                  {subject.questions.length} Questions
                </div>
              </div>
            ))}
          </div>
        </div>
      ) : (
        /* ── QUESTION VIEW ── */
        <div>
          {/* Subject header + score */}
          <div className="glass-panel" style={{ marginBottom: '1.25rem', padding: '0.9rem 1.75rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '0.5rem' }}>
            <h2 className="text-gradient" style={{ fontSize: '1.3rem' }}>{selectedSubject.name}</h2>
            <div style={{ display: 'flex', gap: '1.5rem', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
              <span style={{ color: 'var(--success-color)', fontWeight: '600' }}>✓ {score.correct}</span>
              <span style={{ color: 'var(--error-color)', fontWeight: '600' }}>✗ {score.total - score.correct}</span>
              <span>Total: {score.total}</span>
            </div>
          </div>

          {/* Controls bar */}
          <div className="controls-bar">
            <form onSubmit={handleJump} className="search-box">
              <Hash size={20} style={{ color: 'var(--text-secondary)' }} />
              <input
                type="number"
                className="input-field"
                placeholder={`Jump (1-${questions.length})`}
                value={jumpTo}
                onChange={e => setJumpTo(e.target.value)}
                min="1"
                max={questions.length}
                style={{ width: '160px' }}
              />
              <button type="submit" className="btn btn-primary" style={{ padding: '0.5rem 1rem' }}>Go</button>
            </form>

            <button
              className={`btn ${isShuffled ? 'btn-primary' : ''}`}
              style={{ background: !isShuffled ? 'rgba(255,255,255,0.1)' : '' }}
              onClick={toggleShuffle}
            >
              <Shuffle size={18} /> {isShuffled ? 'Shuffled' : 'Shuffle'}
            </button>

            <button
              className={`btn ${editMode ? 'btn-primary' : ''}`}
              style={{ background: !editMode ? 'rgba(255,255,255,0.1)' : '', border: editMode ? '1px solid var(--warning-color)' : '' }}
              onClick={() => {
                setEditMode(!editMode);
                setAnswered(false); // Reset answer state when entering edit mode
              }}
            >
              <Settings size={18} /> {editMode ? 'Finish Editing' : 'Edit Answer'}
            </button>
          </div>

          {/* Question card */}
          {currentQuestion && (
            <div className="glass-panel question-container">
              {/* Progress */}
              <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text-secondary)', marginBottom: '1rem', fontSize: '0.85rem' }}>
                <span>Question {currentIndex + 1} of {questions.length}</span>
                {!currentQuestion.hasDetectedAnswer && (
                  <span style={{ color: 'var(--warning-color, #f59e0b)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <AlertCircle size={14} /> Answer auto-detected may vary
                  </span>
                )}
              </div>

              {/* Progress bar */}
              <div style={{ height: '4px', background: 'rgba(255,255,255,0.1)', borderRadius: '2px', marginBottom: '1.5rem' }}>
                <div style={{ height: '100%', width: `${((currentIndex + 1) / questions.length) * 100}%`, background: 'var(--primary-color)', borderRadius: '2px', transition: 'width 0.3s ease' }} />
              </div>

              {/* PDF page image or Text Question */}
              <div style={{ borderRadius: '12px', overflow: 'hidden', marginBottom: '1.75rem', border: '1px solid rgba(255,255,255,0.1)' }}>
                {currentQuestion.questionText ? (
                  <div style={{ 
                    padding: '2rem', 
                    background: 'rgba(255,255,255,0.02)', 
                    fontSize: '1.25rem', 
                    lineHeight: '1.6',
                    textAlign: 'center',
                    borderBottom: '1px solid rgba(255,255,255,0.1)'
                  }}>
                    {currentQuestion.questionText}
                    {currentQuestion.image && (
                      <div style={{ marginTop: '1.5rem', background: '#fff', borderRadius: '8px', padding: '1rem', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                        {(Array.isArray(currentQuestion.image) ? currentQuestion.image : [currentQuestion.image]).map((img, i) => (
                          <img 
                            key={i}
                            src={img} 
                            alt={`Question Figure ${i + 1}`} 
                            style={{ maxWidth: '100%', display: 'block', margin: '0 auto', maxHeight: '400px', objectFit: 'contain' }} 
                          />
                        ))}
                      </div>
                    )}
                  </div>
                ) : (
                  <>
                    <img
                      src={currentQuestion.imagePath}
                      alt={`Question ${currentIndex + 1}`}
                      style={{ width: '100%', display: 'block', maxHeight: '65vh', objectFit: 'contain', background: '#fff' }}
                      onError={e => { e.target.style.display = 'none'; e.target.nextSibling.style.display = 'flex'; }}
                    />
                    <div style={{ display: 'none', alignItems: 'center', justifyContent: 'center', height: '200px', color: 'var(--text-secondary)', flexDirection: 'column', gap: '1rem' }}>
                      <AlertCircle size={48} style={{ opacity: 0.4 }} />
                      <p>Image not found. Run extract_mcq.py to generate images.</p>
                    </div>
                  </>
                )}
              </div>

              {/* Answer options A / B / C / D */}
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem', marginBottom: '0.75rem' }}>
                {editMode ? 'Correction Mode: Select the actual correct answer to update data:' : (currentQuestion.questionText ? 'Select the correct option:' : 'Select the correct answer (highlighted green in the PDF above):')}
              </p>
              <div className="options-list" style={{ gridTemplateColumns: currentQuestion.options ? '1fr' : 'repeat(2, 1fr)' }}>
                {OPTION_LABELS.map((label, idx) => (
                  <div
                    key={idx}
                    className={`option-item ${getOptionClass(idx)}`}
                    onClick={() => {
                      if (editMode) {
                        handleSaveCorrection(idx);
                      } else {
                        handleOptionClick(idx);
                      }
                    }}
                    style={{ cursor: (answered && !editMode) ? 'default' : 'pointer', transition: 'all 0.2s', padding: currentQuestion.options ? '1rem 1.5rem' : '1rem' }}
                  >
                    <span className="option-letter">{label}</span>
                    {currentQuestion.options && <span style={{ flexGrow: 1, marginLeft: '0.5rem' }}>{currentQuestion.options[idx]}</span>}
                    {editMode && idx === currentQuestion.correctAnswerIndex && (
                      <CheckCircle size={18} style={{ color: 'var(--success-color)', marginLeft: '6px' }} />
                    )}
                    {!editMode && answered && idx === currentQuestion.correctAnswerIndex && (
                      <CheckCircle size={18} style={{ color: 'var(--success-color)', marginLeft: '6px' }} />
                    )}
                    {!editMode && answered && selectedOption === idx && idx !== currentQuestion.correctAnswerIndex && (
                      <XCircle size={18} style={{ color: 'var(--error-color)', marginLeft: '6px' }} />
                    )}
                  </div>
                ))}
              </div>

              {/* Edit Mode Feedback */}
              {editMode && (
                <div style={{ marginTop: '1rem', display: 'flex', flexDirection: 'column', gap: '0.5rem', alignItems: 'center' }}>
                  {saving && (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--primary-color)' }}>
                      <Loader2 className="animate-spin" size={18} /> Saving to data file...
                    </div>
                  )}
                  {saveMessage.text && (
                    <div style={{ 
                      padding: '0.5rem 1rem', 
                      borderRadius: '6px', 
                      fontSize: '0.9rem',
                      background: saveMessage.type === 'success' ? 'rgba(34,197,94,0.1)' : 'rgba(239,68,68,0.1)',
                      color: saveMessage.type === 'success' ? 'var(--success-color)' : 'var(--error-color)',
                      border: `1px solid ${saveMessage.type === 'success' ? 'var(--success-color)' : 'var(--error-color)'}33`
                    }}>
                      {saveMessage.text}
                    </div>
                  )}
                </div>
              )}

              {/* Feedback message */}
              {answered && (
                <div style={{
                  marginTop: '1rem',
                  padding: '0.75rem 1.25rem',
                  borderRadius: '8px',
                  background: selectedOption === currentQuestion.correctAnswerIndex
                    ? 'rgba(34,197,94,0.15)' : 'rgba(239,68,68,0.15)',
                  color: selectedOption === currentQuestion.correctAnswerIndex
                    ? 'var(--success-color)' : 'var(--error-color)',
                  fontWeight: '600',
                  textAlign: 'center',
                  fontSize: '1rem',
                }}>
                  {selectedOption === currentQuestion.correctAnswerIndex
                    ? '✓ Correct! The answer is ' + OPTION_LABELS[currentQuestion.correctAnswerIndex]
                    : `✗ Incorrect. The correct answer is ${OPTION_LABELS[currentQuestion.correctAnswerIndex]}`}
                </div>
              )}

              {/* Navigation */}
              <div className="nav-buttons" style={{ marginTop: '1.5rem' }}>
                <button className="btn" style={{ background: 'rgba(255,255,255,0.1)' }} onClick={handlePrev} disabled={currentIndex === 0}>
                  <ChevronLeft size={20} /> Previous
                </button>
                <button className="btn btn-primary" onClick={handleNext} disabled={currentIndex === questions.length - 1}>
                  Next <ChevronRight size={20} />
                </button>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
