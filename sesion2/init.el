;;; Package -- Summary
;;; Commentary:
;; Emacs Lisp code for development under python.
;; Provee configuración para facilitar la programación en el lenguaje Python usando Emacs.

;; Modulo para la carga de paquetes de terceros
(require 'package)

;;; Code:

;; Establece la lista de repositorios de donde obtener paquetes para emacs.
(setq package-archives '(("marmalade" . "http://marmalade-repo.org/packages/")
                         ("tromey" . "http://tromey.com/elpa/")
                         ("elpa" . "http://elpa.gnu.org/packages/")
                         ("melpa" . "http://melpa.milkbox.net/packages/")))

;; Permite cargar los repositorios definidos anteriormente
(package-initialize)

;; M-x eval-buffer
;; M-x package-list-packages

;;;;;;;;;;;;;;;;;;;
;; Recordatorios ;;
;;;;;;;;;;;;;;;;;;;

;; C-x C-s Guardar archivo
;; C-x b | C-x C-b Moverse entre buffers

(when (not package-archive-contents)
  (package-refresh-contents))

(defvar my-packages
  '(py-autopep8
    auto-complete helm
    autopair projectile flymake flycheck))

(dolist (p my-packages)
  (when (not (package-installed-p p))
    (package-install p)))

;; M-x eval-buffer
;; M-x emacs-version

;; C-x C-e - Evalua la sección de código actual
(global-linum-mode) ;; Establece el número de linea del lado izquierdo.
(setq column-number-mode t) ;; Pone el número de linea y columna en el modeline.
(setq-default frame-title-format "%b (%f)") ;; Cambiamos el título del Frame.
(global-hl-line-mode 1);; Resalta la linea actual.
(show-paren-mode 1) ;; Resalta el apareamiento de parentesis, llaves, etc.
(require 'flycheck) ;; Permite la verificación de la sintaxis al "vuelo".
(global-flycheck-mode t)
(global-set-key (kbd "C-s") 'isearch-forward-regexp) ;; Actualizamos la forma de buscar
(global-set-key (kbd "C-r") 'isearch-backward-regexp) ;; Busca hacia atras con regex
(global-set-key (kbd "C-M-s") 'isearch-forward) ;; Busquedas por default
(global-set-key (kbd "C-M-r") 'isearch-backward) ;; Busqueda por default
(setq-default indent-tabs-mode nil) ;; No tabuladores duros
(setq x-select-enable-clipboard t
      x-select-enable-primary t
      save-interprogram-paste-before-kill t
      apropos-do-all t
      mouse-yank-at-point t
      backup-directory-alist `(("." . ,(concat user-emacs-directory "backups")))
      auto-save-default nil
      save-place-file (concat user-emacs-directory "places")) ;; Permite la comunicación con el clipboard del sistema

(setq-default save-place t)

(add-hook 'prog-mode-hook
           (lambda ()
             (add-to-list 'write-file-functions 'delete-trailing-whitespace)))
(add-hook 'prog-mode-hook
          (lambda ()
            (add-to-list 'write-file-functions 'delete-blank-lines)))
;; Comentarios
(defun toggle-comment-on-line ()
  "Comenta o descomenta la línea actual."
  (interactive)
  (comment-or-uncomment-region (line-beginning-position) (line-end-position)))
(global-set-key (kbd "C-;") 'toggle-comment-on-line)
(setq create-lockfiles nil)
(setq inhibit-startup-message t)
(require 'auto-complete)
(set-default 'ac-sources
             '(ac-source-abbrev
               ac-source-dictionary
               ac-source-words-in-buffer
               ac-source-words-in-same-mode-buffers
               ac-source-semantic))
(ac-config-default)
(dolist (m '(c-mode c++-mode java-mode org-mode))
  (add-to-list 'ac-modes m))
(global-auto-complete-mode t)
(setq ac-auto-start 2);; auto-complete mode extra settings
(setq ac-use-overriding-local-map nil)
(setq ac-use-menu-map t)
(setq ac-candidate-limit 20)(setq create-lockfiles nil)
(setq inhibit-startup-message t)
(require 'helm)
(setq helm-split-window-in-side-p           t ; open helm buffer inside current window, not occupy whole other window
      helm-move-to-line-cycle-in-source     t ; move to end or beginning of source when reaching top or bottom of source.
      helm-ff-search-library-in-sexp        t ; search for library in `require' and `declare-function' sexp.b
      helm-scroll-amount                    8 ; scroll 8 lines other window using M-<next>/M-<prior>
      helm-ff-file-name-history-use-recentf t)
(global-set-key (kbd "M-x") 'helm-M-x)
(global-set-key (kbd "C-x C-f") 'helm-find-files)
(define-key helm-map (kbd "<tab>") 'helm-execute-persistent-action) ; rebind tab to run persistent action
(define-key helm-map (kbd "C-i") 'helm-execute-persistent-action) ; make TAB works in terminal
(define-key helm-map (kbd "C-z")  'helm-select-action) ; list actions using
(setq helm-M-x-fuzzy-match t)
(global-set-key (kbd "M-y") 'helm-show-kill-ring)
(global-set-key (kbd "C-x b") 'helm-mini)
(require 'py-autopep8);; Las reglas de buena escritura de código.
(require 'autopair);; Pareamiento automático de paréntesis y otros.
(add-to-list 'auto-mode-alist '("\\.py$" . python-mode))
(setq py-electric-colon-active t)
(add-hook 'python-mode-hook 'autopair-mode)
(add-hook 'python-mode-hook 'auto-complete-mode)
(add-hook 'inferior-python-mode-hook (lambda ()
                                       (linum-mode 0)))
(add-hook 'python-mode-hook 'py-autopep8-enable-on-save)
(setq py-autopep8-options '("--max-line-length=100"))
(setq py-autopep8-options '("--inplace"))
(setq py-autopep8-options '("--aggressive"))
(setq py-autopep8-options '("--aggressive"))

(provide 'init)
;;; init.el ends here
